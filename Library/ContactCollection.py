# -*- coding: utf-8 -*-
"""
This function collect all the contact records
marked with "true" in the "allowed_to_collect"
attribute (property) from the Hubspot API and
create a DataFrame with the contacts.
"""
import pandas as pd
import requests

def contactCollection(token):
    #Request headers
    headers = {
        'authorization': 'Bearer pat-na1-3c7b0af9-bb66-40e7-a256-ce4c5eb27e81',
        'content-type': 'application/json'
        }
    
    #Stablish the parameters
    limit = 100
    after = 0
    dataframes = []
    has_more_pages = True
    properties = [
        'raw_email', 'country', 'phone', 
        'technical_test___create_date',
        'industry', 'address', 'hs_object_id'
        ]
    
    #Request all the contact information with 
    #the given parameters 
    while has_more_pages:
        data = {
            #filter that get the contacts in 
            #the allowed_to_collect attribute
            "filters":[{
                    "propertyName": "allowed_to_collect",
                    "operator": "EQ",
                    "value": "true"
                    }],
            "limit":limit,
            "after":after,
            "properties":properties,
            }
    
        #API and data request
        url = 'https://api.hubapi.com/crm/v3/objects/contacts/search'
        response = requests.post(url, json=data, headers=headers)
        data = response.json()
        
        #There are some data columns that are not relevant.
        #Eliminate that colums
        nonRelevant = [
            'id',
            'properties.createdate',
            'properties.lastmodifieddate',
            'createdAt',
            'updatedAt',
            'archived',
            ]
    
        #Normalize and add the information. 
        if 'results' in data:
            results = data['results']
            df = pd.json_normalize(results)
            df.drop(columns=nonRelevant, inplace=True)
            df.rename(columns={'properties.' + prop: prop for prop in properties}, inplace=True)
            dataframes.append(df)
            
        #In case there is a 'paging' indication in the data
        if 'paging' in data:
            paging = data['paging']
            next_page = paging.get('next')
            if next_page:
                after = next_page.get('after')
            else:
                has_more_pages = False
        else:
            has_more_pages = False
        
        #Append all the dataframes
        DataFrame = pd.concat(dataframes, ignore_index=True)
        
        return DataFrame