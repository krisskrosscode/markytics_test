#imports
import json
import os
import warnings
from datetime import date, datetime, timedelta

import pandas as pd
import requests
from sqlalchemy import create_engine

warnings.filterwarnings("ignore")


## auth token 
# from login import auth_token

#db information
user1 = "SFPL_Connect"
password = "$%n5bF33%X"
db = "Sonata_Connect"
server = "172.17.130.216"
engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")

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
    
auth_token = get_authorization()


url = "https://api-smartflo.tatateleservices.com/v1/call/records"

headers = {"accept": "application/json", "Authorization" : auth_token}

response = requests.get(url, headers=headers)

data = pd.json_normalize(response.json())
# data = data[['id', 'lead_id', 'list_id','field_0', 'field_1', 'field_2', 'field_3','field_4', 'field_5','dial_status']]
# print(data)
print(data.columns)

print(data['results'])