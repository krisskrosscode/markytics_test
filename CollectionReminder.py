import pandas as pd
from sqlalchemy import create_engine
import os
import requests
from datetime import datetime, timedelta
import warnings 
warnings.filterwarnings('ignore')

#fetch queue data and other necessary data required
user1 = "SFPL_Connect"
password = "$%n5bF33%X"
db = "Sonata_Connect"
server = "172.17.130.216"
engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")


# obtain whatsapp queue rows 
queue_sql_query = f""" SELECT * FROM Sonata_Connect.dbo.WhatsAppQueue 
WHERE status = 'running' """
queue_df = pd.read_sql_query(queue_sql_query,engine)

## obtain all calling issues
# ci_sql_query = f"""SELECT * FROM Sonata_Connect.dbo.CallingIssues """
# calling_issues_df =  pd.read_sql_query(ci_sql_query, engine)

# print(calling_issues_df)

# queue_df = pd.merge(left=queue_df, right=calling_issues_df, how='left', left_on='contact_number', right_on='customer_number').drop('id_x', axis=1)

## get queue columns
customer_number = queue_df['customer_number']
field1 = queue_df['field_1']
field2 = queue_df['field_2']
field3 = queue_df['field_3']
field4 = queue_df['field_4']
field5 = queue_df['field_5']
field6 = queue_df['field_6']
field7 = queue_df['field_7']
field8 = queue_df['field_8']
field9 = queue_df['field_9']
field10 = queue_df['field_10']


## send alert
url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={customer_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%86%E0%A4%88%E0%A4%A1%E0%A5%80%3A+{field1}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%AE%E0%A4%BE%E0%A4%A8+{field2}%28{field3}%29+%E0%A4%B8%E0%A5%87+%E0%A4%8F%E0%A4%95+%E0%A4%A8%E0%A4%AF%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B8%E0%A5%8C%E0%A4%82%E0%A4%AA%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{field4}%28{field5}%29%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A5%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%A4%E0%A4%BE+{field6}+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%95%E0%A5%80+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%E0%A4%B8%E0%A5%80%E0%A4%AE%E0%A4%BE+%E0%A4%B9%E0%A5%88+{field7}%2C{field8}%0A%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+%E0%A4%8F%E0%A4%95%E0%A4%A4%E0%A5%8D%E0%A4%B0+%E0%A4%95%E0%A5%80+%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A5%80+%E0%A4%B9%E0%A5%88+{field9}%0A%E0%A4%B8%E0%A4%82%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%B9+%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8+{field10}%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA+%E0%A4%87%E0%A4%B8+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%95%E0%A5%8B+%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A4%BE+%E0%A4%95%E0%A4%B0+%E0%A4%AA%E0%A4%BE%E0%A4%8F%E0%A4%82%E0%A4%97%E0%A5%87%3F&isTemplate=true&header=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4%BE%E0%A4%B8+%E0%A4%8F%E0%A4%95+%E0%A4%A8%E0%A4%AF%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%88"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)