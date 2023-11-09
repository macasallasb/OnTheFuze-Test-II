"""
This function store the collected contacts with their
respective transformed data in HubSpot.
"""

import requests

def savingContacts(df, token, delete_none_emails=True):
    if delete_none_emails:
        df = df[df['raw_email'] != 'None']
    df['address'] = df['address'].fillna("None")
    df['country'] = df['country'].fillna("None")
    df['phone'] = df['phone'].fillna("None")
    
    url = 'https://api.hubapi.com/crm/v3/objects/contacts'
    
    #Handle potential rate limited by batching requests
    batch_size = 10
    batches = [df[i:i+batch_size] for i in range(0, len(df), batch_size)]

    headers = {
        'authorization': 'Bearer pat-na1-3c7b0af9-bb66-40e7-a256-ce4c5eb27e81',
        'content-type': 'application/json'
    }
    
    #Upload contact counter
    success_count = 0  
    for batch in batches:
        contacts = []
        for _, row in batch.iterrows():
            #json payload for each contact
            contact = {
                "properties": {
                    "email": row['raw_email'],
                    "phone": row['phone'],
                    "country": row['country'],
                    "city": row['city'],
                    "original_create_date": row['technical_test___create_date'],
                    "original_industry": row['industry'],
                    "temporary_id": row['hs_object_id'],
                    "address": row['address']
                }
            }
            contacts.append(contact)

        #Request body with a list of contacts
        body = {"inputs": contacts}

        try:
            #POST request to upload the contacts to the HubSpot API
            response = requests.post(url, headers=headers, json=body)
            # Check for request errors
            response.raise_for_status()  
            success_count += len(contacts)  
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    message = f"{success_count} contacts imported to Hubspot successfully"

    return message