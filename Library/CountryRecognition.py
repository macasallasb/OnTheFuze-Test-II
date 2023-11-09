"""
This function recognizes if the record value 
corresponds to a country or a city.

In the case it´s a city the output will be a 
tuple(country_found, city_found).
In the case it´s a country the output will be a
tuple(country_found, ' ').
"""

import pandas as pd

def countryRecognition(df):
    Dictionary_Cities = {
        "England": ["London", "Milton Keynes", "Oxford", "Plymouth", "Winchester"],
        "Ireland": ["Dublin", "Cork", "Limerick", "Waterford"]
            }
    
    #Create a set of all the cities
    cities = set(city for cities_list in Dictionary_Cities.values() for city in cities_list)
    
    def locationRecognition(location):
        if location in Dictionary_Cities:
            return location, None
        elif location in cities:
            for country, city_list in Dictionary_Cities.items():
                if location in city_list:
                    return country, location
        return None, None
    
    #Apply the 'locationRecognition' function to the 'country' column 
    #and expand the result into two separate columns which are 
    #'country' and 'city'
    df[["country", "city"]] = df["country"].apply(locationRecognition).apply(pd.Series)
    #Lambda function let
    df["country, city"] = df.apply(lambda x: (x["country"], x["city"]) if x["country"] is not None else (None, None), axis=1)
    df['name'] = df['firstname'].astype(str) + df['lastname'].astype(str)
    df.drop(columns='city', inplace=True)
    #df.drop(columns='country', inplace=True)
    
    return df