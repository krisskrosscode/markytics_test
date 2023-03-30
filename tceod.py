#imports
import os
import warnings
from datetime import datetime, timedelta,date

import pandas as pd
import requests
from sqlalchemy import create_engine

warnings.filterwarnings("ignore")

#db information
user1 = "SFPL_Connect"
password = "$%n5bF33%X"
db = "Sonata_Connect"
server = "172.17.130.216"
engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")

#auth function
def get_authorization():
    username = os.environ['PAYMEE_SONATA_TATA_USERNAME']
    password = os.environ['PAYMEE_SONATA_TATA_PASSWORD']
    print(username,password)
    url = "https://api-smartflo.tatateleservices.com/v1/auth/login"

    payload = {
        "email": username,
        "password": password
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['access_token']
    else :
        return None

#fromdate and todate, specifying width of the data to be taken in
# from_date = datetime.now() - timedelta(days=1)
# to_date = datetime.now()
# from_date='2023-03-28'
# to_date='2023-03-29'
# 2023-03-28 16:12:10.243116 2023-03-29 16:12:10.243116
from_date = date.today() - timedelta(days=1)
to_date = date.today()
print(from_date,to_date)
# 2023-03-28 2023-03-29
#api setup
url = "https://api-smartflo.tatateleservices.com/v1/call/records"
auth_token = get_authorization()
headers = {
    "Accept": "application/json",
    "Authorization": f"{auth_token}"
}
params = {
    'from_date': from_date,
    'to_date': to_date,
    'limit':100
}
response = requests.get(url, headers=headers,params=params)

#recieved data
data = pd.json_normalize(response.json()['results'])
print(len(data))
#data prep
count = response.json()['count']
print(count)
if count > 100:
    page_numbers = count // 100
    print(page_numbers)
    remainder_pages = count % 100
    print(remainder_pages)

    if page_numbers > 1 :
        for i in range(2,page_numbers+1):
            print('page:', i)

            params = {
                'from_date': from_date,
                'to_date': to_date,
                'limit':100,
                'page':i
            }
            response = requests.get(url, headers=headers,params=params)
            data_append = pd.json_normalize(response.json()['results'])
            data = data.append(data_append)

    if remainder_pages > 0:
        params = {
            'from_date': from_date,
            'to_date': to_date,
            'limit':100,
            'page':page_numbers + 1
        }
        response = requests.get(url, headers=headers,params=params)
        data_append = pd.json_normalize(response.json()['results'])[:remainder_pages]
        data = data.append(data_append)
print("Stage1")
if count > 0:
    final_df = data[['call_id',
            'uuid',
            'direction',
            'description',
            'status',
            'recording_url',
            'service',
            'date',
            'time',
            'end_stamp',
            'call_duration',
            'answered_seconds',
            'minutes_consumed',
            'agent_number',
            'agent_name',
            'client_number',
            'did_number',
            'reason',
            'hangup_cause',
            'accountid',
            'circle.operator',
            'circle.circle']]
final_df.rename(columns = {'circle.operator':'circle_operator', 'circle.circle':'circle_circle'}, inplace = True)
for col in ['client_number','agent_number','did_number']:
    final_df[col] = final_df[col].apply(lambda x: str(x)[-10:])
print("Saving Stage")
#store logic
final_df.to_sql('tata_calling_EOD', con=engine, if_exists='append',index=False)

name = 'E:\logs/eod_scheduler_log.txt'
with open(name, 'a') as file:
    file.write(str(datetime.now()))
    file.write('---')
