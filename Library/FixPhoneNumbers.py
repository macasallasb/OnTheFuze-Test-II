"""
This function add the 'country phone cody', according to the detected country, 
to the phone number.

The output will be a string with the fixed phone number with the 
'(+XXX) XXXX XXXXXX' format.
"""

def fixPhoneNumbers(df):
    countryCodes = {
        'England': '+44',
        'Ireland': '+353',
    }
    
    def fixPhone(phone, countryCode):
        if phone is not None and countryCode is not None:
            #Remove whitespaces and hyphens
            phone = phone.replace("-", "").replace(" ", "")
            #Add the variable 'countryCode' to the phone 
            phone = f"({countryCode}) {phone}"
        return phone
    
    df["phone"] = df.apply(lambda row: fixPhone(row["phone"], countryCodes.get(row["country"], "")), axis=1)

    return df
