"""
This function groups the contacts with the same email
and the following considerations:
    If an old record contains data that the new one
    doesn´t, the function add it to the most recent
    record.
    The function rewrites the most recent contact
    information.
"""

import pandas as pd

def duplicatesManagement(df):
    # Temporal copy of the dataframe
    temporal_df = df.copy()
    
    #Sort the dataframe by 'name' and 'technical_test___create_date' in descending order
    temporal_df.sort_values(["name", "technical_test___create_date"], ascending=[True, False], inplace=True)
    temporal_df['raw_email'] = temporal_df.groupby('name')['raw_email'].transform('first')
    temporal_df.reset_index(drop=True, inplace=True)

    #Sort the dataframe by 'raw_email' and 
    #'technical_test___create_date' in descending 
    #order
    temporal_df.sort_values(["raw_email", "technical_test___create_date"], ascending=[True, False], inplace=True)
    

    #Group the information in the 'industry' column 
    #in case the contact has more than one industry
    temporal_df['industry'] = temporal_df.groupby('raw_email')['industry'].transform(lambda x: ';'.join(x.drop_duplicates()))
    temporal_df['industry'] = temporal_df['industry'].apply(lambda x: ";" + x if isinstance(x, str) and ";" in x else x)
    
    #Identify and get the last address, country and 
    #phone for each group of an email, respectively  
    temporal_df['address'] = temporal_df.groupby('raw_email')['address'].transform('first')
    temporal_df['country'] = temporal_df.groupby('raw_email')['country'].transform('first')
    temporal_df['phone'] = temporal_df.groupby('raw_email')['phone'].transform('first')
    

    #Drop the 'raw_email'column duplicates 
    temporal_df.drop_duplicates(subset=['raw_email'], keep='first', inplace=True)
    temporal_df = temporal_df[temporal_df['name'].notna()]
    temporal_df.reset_index(drop=True, inplace=True)
    temporal_df.drop(columns='country, city', inplace=True)

    return temporal_df