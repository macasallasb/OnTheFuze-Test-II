"""
This function extracts only the email from the column
'raw_email'.
"""

import pandas as pd
import re

def foundEmails(df):
    #Lambda function takes an email value from the
    #column "raw_email" and verifies that the email
    #has the form <email>, in that case the email is
    #extracted.
    df["raw_email"] = df["raw_email"].apply(lambda email: re.search(r'<(.+)>', email).group(1) if pd.notna(email) and re.search(r'<(.+)>', email) else email)
    return df