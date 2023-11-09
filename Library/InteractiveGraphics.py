"""
This code is encharged of the dataframe analysis.
The idea is to analize and observe the contacts 
based on their country residence, and for each
country to analize the periods in which the 
contact creation is higher.
"""

#Date Analysis

#By day
import plotly.express as px
# Group the data by day and count the number of contacts
contact_counts = DF.groupby('technical_test___create_date')['country'].count().reset_index()
# Create the line chart
fig = px.line(contact_counts, x='technical_test___create_date', y='country', title='Daily contact log during 2021')
# Customize the chart layout
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Número de Contactos',
)
fig.show()



#By month
import panda as pd
import plotly.express as px

#Transform the column to datetime
DF['technical_test___create_date'] = pd.to_datetime(DF['technical_test___create_date'])
monthGroup = DF.groupby(dfDuplicates['technical_test___create_date'].dt.month).size()
#Create a month dictionary
month = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
    'September', 'October','November', 'December'
    ]
monthValues = monthGroup.values.tolist()
# Create the line chart
fig = px.line(contact_counts, x='Month', y='country', title='Monthly Contact log during 2021')
# Customize the chart layout
fig.update_xaxes(type='category')  # Ensure correct date display
fig.update_layout(
    xaxis_title='Month',
    yaxis_title='Number of Contacts',
)
fig.show()






