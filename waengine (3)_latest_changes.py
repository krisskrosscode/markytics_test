#necessary imports
import pandas as pd
from sqlalchemy import create_engine
import os
import requests
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")

#fetch queue data and other necessary data required
user1 = "SFPL_Connect"
password = "$%n5bF33%X"
db = "Sonata_Connect"
server = "172.17.130.216"
engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")

sql_query = f""" SELECT * FROM Sonata_Connect.dbo.WhatsAppQueue 
WHERE status = 0 or status = 1 or status IS NULL """
queue_df=pd.read_sql_query(sql_query,engine)

#filter queue by status, unique on userid and keep the first after ordering by id
queue_df.sort_values(by='id', inplace=True)
queue_df.drop_duplicates(subset = 'user_id', keep='first', inplace=True)
queue_df.to_csv('papa.csv')

#prepare all the APIs on standby, required to send all kind of messages
#prepare functions with parameters, so that we can pick data from queue table and supply them when needed to be sent
#Collection Followup
#on task create alert - 1
def cfu_1(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    # print(response.text)
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%86%E0%A4%88%E0%A4%A1%E0%A5%80%3A+{f1}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%AE%E0%A4%BE%E0%A4%A8+{f2}%28{f3}%29+%E0%A4%B8%E0%A5%87+%E0%A4%8F%E0%A4%95+%E0%A4%A8%E0%A4%AF%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B8%E0%A5%8C%E0%A4%82%E0%A4%AA%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f4}%28{f5}%29%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A5%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%A4%E0%A4%BE+{f6}+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%95%E0%A5%80+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%E0%A4%B8%E0%A5%80%E0%A4%AE%E0%A4%BE+%E0%A4%B9%E0%A5%88+{f7}%2C{f8}%0A%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+%E0%A4%8F%E0%A4%95%E0%A4%A4%E0%A5%8D%E0%A4%B0+%E0%A4%95%E0%A5%80+%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A5%80+%E0%A4%B9%E0%A5%88+{f9}%0A%E0%A4%B8%E0%A4%82%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%B9+%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8+{f10}%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA+%E0%A4%87%E0%A4%B8+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%95%E0%A5%8B+%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A4%BE+%E0%A4%95%E0%A4%B0+%E0%A4%AA%E0%A4%BE%E0%A4%8F%E0%A4%82%E0%A4%97%E0%A5%87%3F&isTemplate=true&header=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4%BE%E0%A4%B8+%E0%A4%8F%E0%A4%95+%E0%A4%A8%E0%A4%AF%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%88"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)
    # print(response.text)
#ask date alert - 3
def cfu_2(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%AF%E0%A4%BE%E0%A4%A6+%E0%A4%A6%E0%A4%BF%E0%A4%B2%E0%A4%BE%E0%A4%AF%E0%A4%BE+%E0%A4%9C%E0%A4%BE%E0%A4%A4%E0%A4%BE+%E0%A4%B9%E0%A5%88+%E0%A4%95%E0%A5%87+%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4%BE%E0%A4%B8+%E0%A4%86%E0%A4%97%E0%A4%BE%E0%A4%AE%E0%A5%80+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%8F%E0%A4%95+%E0%A4%95%E0%A4%B2%E0%A5%87%E0%A4%95%E0%A5%8D%E0%A4%B6%E0%A4%A8+%E0%A4%95%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%88%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%86%E0%A4%88%E0%A4%A1%E0%A5%80%3A+{f1}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%AE%E0%A4%BE%E0%A4%A8+{f2}%28{f3}%29+%E0%A4%B8%E0%A5%87+%E0%A4%8F%E0%A4%95+%E0%A4%A8%E0%A4%AF%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B8%E0%A5%8C%E0%A4%82%E0%A4%AA%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f4}%28{f5}%29%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A5%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%A4%E0%A4%BE+{f6}+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%95%E0%A5%80+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%E0%A4%B8%E0%A5%80%E0%A4%AE%E0%A4%BE+%E0%A4%B9%E0%A5%88+{f7}%2C{f8}%0A%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+%E0%A4%8F%E0%A4%95%E0%A4%A4%E0%A5%8D%E0%A4%B0+%E0%A4%95%E0%A5%80+%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A5%80+%E0%A4%B9%E0%A5%88+{f9}%0A%E0%A4%B8%E0%A4%82%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%B9+%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8+{f10}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    url = f"https://sarthi.sonataindia.com/running_to_incomplete/{id}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
#thank you for accepting alert
def cfu_3(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%86%E0%A4%88%E0%A4%A1%E0%A5%80%3A+{f1}%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f4}%28{f5}%29%0A%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+%E0%A4%8F%E0%A4%95%E0%A4%A4%E0%A5%8D%E0%A4%B0+%E0%A4%95%E0%A5%80+%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A5%80+%E0%A4%B9%E0%A5%88+{f9}%0A%E0%A4%B8%E0%A4%82%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%B9+%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8+{f10}%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA%E0%A4%A8%E0%A5%87+%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+%E0%A4%8F%E0%A4%95%E0%A4%A4%E0%A5%8D%E0%A4%B0+%E0%A4%95%E0%A5%80+%E0%A4%B9%E0%A5%88%3F&isTemplate=true&header=%E0%A4%B8%E0%A4%82%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%B9+%E0%A4%95%E0%A5%80+%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%A4%E0%A4%BF"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    # response = requests.request("GET", url, headers=headers, data=payload)
    url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)


def ret_1(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """Retention Followup"""
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3+%3A+{f1}+%28{f2}%29%0A%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A4%BF%E0%A4%A4+%E0%A4%8B%E0%A4%A3+%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+{f3}+%E0%A4%8B%E0%A4%A3+%E0%A4%95%E0%A4%BE+%E0%A4%89%E0%A4%A6%E0%A5%8D%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A5%8D%E0%A4%AF+{f4}%0A%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A5%87%E0%A4%9C+%E0%A4%9C%E0%A4%AE%E0%A4%BE+%E0%A4%95%E0%A4%B0%E0%A4%B5%E0%A4%BE%E0%A4%8F+%E0%A4%B9%E0%A5%88%E0%A4%82+%3F+{f5}%0A%E0%A4%B8%E0%A4%B9-%E0%A4%86%E0%A4%B5%E0%A5%87%E0%A4%A6%E0%A4%95+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f6}+%0A%E0%A4%AC%E0%A5%88%E0%A4%82%E0%A4%95+%E0%A4%96%E0%A4%BE%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f7}%0A%E0%A4%AA%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f8}%0A%E0%A4%86%E0%A4%AA+%E0%A4%95%E0%A4%BF%E0%A4%B8+%E0%A4%A4%E0%A4%BE%E0%A4%B0%E0%A5%80%E0%A4%96+%E0%A4%95%E0%A5%8B+%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B8%E0%A5%87+%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%95+%E0%A4%95%E0%A4%B0%E0%A5%87%E0%A4%82%E0%A4%97%E0%A5%87++%3F%0A%28%E0%A4%89%E0%A4%A6%E0%A4%BE%E0%A4%B9%E0%A4%B0%E0%A4%A3+%E0%A4%95%E0%A5%87+%E0%A4%B2%E0%A4%BF%E0%A4%8F%2C+%E0%A4%AF%E0%A4%A6%E0%A4%BF+%E0%A4%86%E0%A4%AA+19+%E0%A4%AB%E0%A4%B0%E0%A4%B5%E0%A4%B0%E0%A5%80+2023+%E0%A4%95%E0%A5%8B+%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B9%E0%A4%95+%E0%A4%B8%E0%A5%87+%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%95++%E0%A4%95%E0%A4%B0+%E0%A4%B8%E0%A4%95%E0%A4%A4%E0%A5%87+%E0%A4%B9%E0%A5%88%E0%A4%82%2C+%E0%A4%A4%E0%A5%8B+190223+%E0%A4%A6%E0%A4%B0%E0%A5%8D%E0%A4%9C+%E0%A4%95%E0%A4%B0%E0%A5%87%E0%A4%82&isTemplate=true&header=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4%BE%E0%A4%B8+%E0%A4%8F%E0%A4%95+%E0%A4%A8%E0%A4%AF%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%88"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    # response = requests.request("GET", url, headers=headers, data=payload)
    url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)


def ret_2(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """Retention Reminder"""
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&password=z24gzBUA&msg=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%AF%E0%A4%BE%E0%A4%A6+%E0%A4%A6%E0%A4%BF%E0%A4%B2%E0%A4%BE%E0%A4%AF%E0%A4%BE+%E0%A4%9C%E0%A4%BE%E0%A4%A4%E0%A4%BE+%E0%A4%B9%E0%A5%88+%E0%A4%95%E0%A5%87+%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4%BE%E0%A4%B8+%E0%A4%86%E0%A4%97%E0%A4%BE%E0%A4%AE%E0%A5%80+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%8F%E0%A4%95+%E0%A4%B0%E0%A4%BF%E0%A4%9F%E0%A5%87%E0%A4%82%E0%A4%B6%E0%A4%A8+%E0%A4%B8%E0%A4%82%E0%A4%AC%E0%A4%82%E0%A4%A7%E0%A5%80+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%88%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3+%3A+{f1}+%28{f2}%29%0A%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A4%BF%E0%A4%A4+%E0%A4%8B%E0%A4%A3+%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+{f3}%0A%E0%A4%8B%E0%A4%A3+%E0%A4%95%E0%A4%BE+%E0%A4%89%E0%A4%A6%E0%A5%8D%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A5%8D%E0%A4%AF+{f4}%0A%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A5%87%E0%A4%9C+%E0%A4%9C%E0%A4%AE%E0%A4%BE+%E0%A4%95%E0%A4%B0%E0%A4%B5%E0%A4%BE%E0%A4%8F+%E0%A4%B9%E0%A5%88%E0%A4%82+%3F+{f5}%0A%E0%A4%B8%E0%A4%B9-%E0%A4%86%E0%A4%B5%E0%A5%87%E0%A4%A6%E0%A4%95+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f6}+%0A%E0%A4%AC%E0%A5%88%E0%A4%82%E0%A4%95+%E0%A4%96%E0%A4%BE%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f7}%0A%E0%A4%AA%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f8}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    # response = requests.request("GET", url, headers=headers, data=payload)
    url = f'https://sarthi.sonataindia.com/running_to_incomplete/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)


def ret_3(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """Retention Confirmation"""
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f1}+%28{f2}%29%0A%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A4%BF%E0%A4%A4+%E0%A4%8B%E0%A4%A3+%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+{f3}%0A%E0%A4%8B%E0%A4%A3+%E0%A4%95%E0%A4%BE+%E0%A4%89%E0%A4%A6%E0%A5%8D%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A5%8D%E0%A4%AF+{f4}%0A%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A5%87%E0%A4%9C+%E0%A4%9C%E0%A4%AE%E0%A4%BE+%E0%A4%95%E0%A4%B0%E0%A4%B5%E0%A4%BE%E0%A4%8F+%E0%A4%B9%E0%A5%88%E0%A4%82+%3F+{f5}%0A%E0%A4%AC%E0%A5%88%E0%A4%82%E0%A4%95+%E0%A4%96%E0%A4%BE%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f6}%0A%E0%A4%B8%E0%A4%B9-%E0%A4%86%E0%A4%B5%E0%A5%87%E0%A4%A6%E0%A4%95+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f7}+%0A%E0%A4%AA%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f8}%0A%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA%E0%A4%A8%E0%A5%87+%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B9%E0%A4%95+%E0%A4%B8%E0%A5%87+%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%95+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F&isTemplate=true&header=%E0%A4%B0%E0%A4%BF%E0%A4%9F%E0%A5%87%E0%A4%82%E0%A4%B6%E0%A4%A8+%E0%A4%95%E0%A5%80+%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%A4%E0%A4%BF"
    # url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f1}+%28{f2}%29%0A%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A4%BF%E0%A4%A4+%E0%A4%8B%E0%A4%A3+%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+{f3}%0A%E0%A4%8B%E0%A4%A3+%E0%A4%95%E0%A4%BE+%E0%A4%89%E0%A4%A6%E0%A5%8D%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A5%8D%E0%A4%AF+{f4}%0A%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A5%87%E0%A4%9C+%E0%A4%9C%E0%A4%AE%E0%A4%BE+%E0%A4%95%E0%A4%B0%E0%A4%B5%E0%A4%BE%E0%A4%8F+%E0%A4%B9%E0%A5%88%E0%A4%82+%3F+{f5}%0A%E0%A4%B8%E0%A4%B9-%E0%A4%86%E0%A4%B5%E0%A5%87%E0%A4%A6%E0%A4%95+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f6}+%0A%E0%A4%AC%E0%A5%88%E0%A4%82%E0%A4%95+%E0%A4%96%E0%A4%BE%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f7}%0A%E0%A4%AA%E0%A4%A4%E0%A5%87+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%AC%E0%A4%A6%E0%A4%B2%E0%A4%BE%E0%A4%B5+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F+{f8}%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA%E0%A4%A8%E0%A5%87+%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B9%E0%A4%95+%E0%A4%B8%E0%A5%87+%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%95+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F&isTemplate=true&header=%E0%A4%B0%E0%A4%BF%E0%A4%9F%E0%A5%87%E0%A4%82%E0%A4%B6%E0%A4%A8+%E0%A4%95%E0%A5%80+%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%A4%E0%A4%BF"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    # response = requests.request("GET", url, headers=headers, data=payload)
    url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)


def WNAP_alert(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """ Alert Q created If alternate number is present """
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&password=z24gzBUA&msg=%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF+{f1}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%95%E0%A4%BE+%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%A8%E0%A4%BE+%E0%A4%B9%E0%A5%88%E0%A5%A4++%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3+%3A+{f2}+%28{f3}%29%0A%E0%A4%B5%E0%A5%88%E0%A4%95%E0%A4%B2%E0%A5%8D%E0%A4%AA%E0%A4%BF%E0%A4%95+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%3A+{f4}%0A%E0%A4%95%E0%A5%83%E0%A4%AA%E0%A4%AF%E0%A4%BE+%E0%A4%87%E0%A4%B8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%AA%E0%A4%B0+%E0%A4%95%E0%A5%89%E0%A4%B2+%E0%A4%95%E0%A4%B0%E0%A5%87%E0%A4%82%E0%A5%A4"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    url = f'https://sarthi.sonataindia.com/running_to_incomplete/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)

def WNAP_flow(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """ If alternate number is present """
    print('thi sis running')
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&isTemplate=true&password=z24gzBUA&msg=%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF+{f1}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%95%E0%A4%BE+%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%A8%E0%A4%BE+%E0%A4%A5%E0%A4%BE%E0%A5%A4+%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f2}+%28{f3}%29%0A%E0%A4%B5%E0%A5%88%E0%A4%95%E0%A4%B2%E0%A5%8D%E0%A4%AA%E0%A4%BF%E0%A4%95+%E0%A4%AB%E0%A4%BC%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%3A+{f4}%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA%E0%A4%A8%E0%A5%87+%E0%A4%87%E0%A4%B8+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF++%E0%A4%95%E0%A5%8B+%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A4%BE+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%3F"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)
    print(response.text)

def WNV_alert(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """ Flow to begin when Agent Visits the Customer  """
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%AF%E0%A4%BE%E0%A4%A6+%E0%A4%A6%E0%A4%BF%E0%A4%B2%E0%A4%BE%E0%A4%AF%E0%A4%BE+%E0%A4%9C%E0%A4%BE%E0%A4%A4%E0%A4%BE+%E0%A4%B9%E0%A5%88+%E0%A4%95%E0%A4%BF+%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%87%E0%A4%A4%E0%A5%81+%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B8%E0%A5%87+%E0%A4%B5%E0%A5%8D%E0%A4%AF%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BF%E0%A4%97%E0%A4%A4+%E0%A4%B0%E0%A5%82%E0%A4%AA+%E0%A4%B8%E0%A5%87+%E0%A4%AE%E0%A4%BF%E0%A4%B2%E0%A4%A8%E0%A4%BE+%E0%A4%B9%E0%A5%88%E0%A5%A4+%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3+%3A+{f2}+%28{f3}%29%0A%E0%A4%AE%E0%A4%BF%E0%A4%B2%E0%A4%A8%E0%A5%87+%E0%A4%95%E0%A5%80+%E0%A4%A4%E0%A4%BE%E0%A4%B0%E0%A5%80%E0%A4%96+%3A+{f5}%0A%E0%A4%AE%E0%A4%BF%E0%A4%B2%E0%A4%A8%E0%A5%87+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%3A+{f6}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    url = f'https://sarthi.sonataindia.com/running_to_incomplete/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)

def WNV_flow(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """ Flow to begin when Agent Visits the Customer  """
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF+{f1}%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA%E0%A4%A8%E0%A5%87+%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B8%E0%A5%87+%E0%A4%B5%E0%A5%8D%E0%A4%AF%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BF%E0%A4%97%E0%A4%A4+%E0%A4%B0%E0%A5%82%E0%A4%AA+%E0%A4%B8%E0%A5%87+%E0%A4%AE%E0%A4%BF%E0%A4%B2%E0%A4%95%E0%A4%B0+%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%3F%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3+%3A+{f2}+%28{f3}%29&isTemplate=true"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)

def WNANP_flow(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    """ If alternate number is NOT present """
    print('WNANp flowwww')
    url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF+{f1}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4%BE%E0%A4%B8+%E0%A4%8F%E0%A4%95+%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0+%E0%A4%B8%E0%A4%82%E0%A4%AC%E0%A4%82%E0%A4%A7%E0%A5%80+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%88%E0%A5%A4+%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B8%E0%A5%87+%E0%A4%B5%E0%A5%8D%E0%A4%AF%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BF%E0%A4%97%E0%A4%A4+%E0%A4%B0%E0%A5%82%E0%A4%AA+%E0%A4%B8%E0%A5%87+%E0%A4%AE%E0%A4%BF%E0%A4%B2%E0%A4%95%E0%A4%B0+%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0+%E0%A4%95%E0%A4%B0%E0%A4%A8%E0%A4%BE+%E0%A4%B9%E0%A5%88%E0%A5%A4+%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3+%3A+{f2}+%28{f3}%29%0A%E0%A4%86%E0%A4%AA+%E0%A4%95%E0%A5%80+%E0%A4%A4%E0%A4%BE%E0%A4%B0%E0%A5%80%E0%A4%96+%E0%A4%95%E0%A5%8B+%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B8%E0%A5%87+%E0%A4%AE%E0%A4%BF%E0%A4%B2+%E0%A4%B8%E0%A4%95%E0%A4%A4%E0%A5%87+%E0%A4%B9%E0%A5%88+%3F%0A%28%E0%A4%89%E0%A4%A6%E0%A4%BE%E0%A4%B9%E0%A4%B0%E0%A4%A3+%E0%A4%95%E0%A5%87+%E0%A4%B2%E0%A4%BF%E0%A4%8F%2C+%E0%A4%AF%E0%A4%A6%E0%A4%BF+%E0%A4%86%E0%A4%AA+18+%E0%A4%AB%E0%A4%B0%E0%A4%B5%E0%A4%B0%E0%A5%80+2023+%E0%A4%95%E0%A5%8B+%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B9%E0%A4%95+%E0%A4%B8%E0%A5%87+%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%95++%E0%A4%95%E0%A4%B0+%E0%A4%B8%E0%A4%95%E0%A4%A4%E0%A5%87+%E0%A4%B9%E0%A5%88%E0%A4%82%2C+%E0%A4%A4%E0%A5%8B+180223+%E0%A4%A6%E0%A4%B0%E0%A5%8D%E0%A4%9C+%E0%A4%95%E0%A4%B0%E0%A5%87%E0%A4%82"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
    response = requests.request("POST", url)
    print(response.text)


# def WN_P_Reminder(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
#     """Reminder Template when alternate number is NOT present"""
#     url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%AF%E0%A4%BE%E0%A4%A6+%E0%A4%A6%E0%A4%BF%E0%A4%B2%E0%A4%BE%E0%A4%AF%E0%A4%BE+%E0%A4%9C%E0%A4%BE%E0%A4%A4%E0%A4%BE+%E0%A4%B9%E0%A5%88+%E0%A4%95%E0%A5%87+%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4%BE%E0%A4%B8+%E0%A4%86%E0%A4%97%E0%A4%BE%E0%A4%AE%E0%A5%80+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%E0%A4%AE%E0%A5%87%E0%A4%82+%E0%A4%8F%E0%A4%95+%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0+%E0%A4%95%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B9%E0%A5%88%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%86%E0%A4%88%E0%A4%A1%E0%A5%80%3A+{f1}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B+%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%AE%E0%A4%BE%E0%A4%A8+{f2}%28{f3}%29+%E0%A4%B8%E0%A5%87+%E0%A4%8F%E0%A4%95+%E0%A4%A8%E0%A4%AF%E0%A4%BE+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%B8%E0%A5%8C%E0%A4%82%E0%A4%AA%E0%A4%BE+%E0%A4%97%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f4}%28{f5}%29%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A5%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%A4%E0%A4%BE+{f6}+%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%95%E0%A5%80+%E0%A4%B8%E0%A4%AE%E0%A4%AF+%E0%A4%B8%E0%A5%80%E0%A4%AE%E0%A4%BE+%E0%A4%B9%E0%A5%88+{f7}%2C{f8}%0A%E0%A4%B5%E0%A5%88%E0%A4%95%E0%A4%B2%E0%A5%8D%E0%A4%AA%E0%A4%BF%E0%A4%95+%E0%A4%AB%E0%A4%BC%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+{f10}&isTemplate=true"
#     payload={}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     print(response.text)
#     url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
#     response = requests.request("POST", url)


# def WN_P_Confirmation(id,user_number,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
#     """Confirmation Template when alternate number is NOT present"""
#     url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF+%E0%A4%86%E0%A4%88%E0%A4%A1%E0%A5%80%3A+{f1}%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE+%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A+{f3}%28{f4}%29%0A%E0%A4%B5%E0%A5%88%E0%A4%95%E0%A4%B2%E0%A5%8D%E0%A4%AA%E0%A4%BF%E0%A4%95+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%3A+{f10}%0A%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE+%E0%A4%86%E0%A4%AA%E0%A4%A8%E0%A5%87+%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B9%E0%A4%95+%E0%A4%B8%E0%A5%87+%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%95+%E0%A4%95%E0%A4%BF%E0%A4%AF%E0%A4%BE+%E0%A4%B9%E0%A5%88+%3F&isTemplate=true&header=%E0%A4%97%E0%A4%B2%E0%A4%A4+%E0%A5%9E%E0%A5%8B%E0%A4%A8+%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0+%E0%A4%B8%E0%A5%81%E0%A4%A7%E0%A4%BE%E0%A4%B0+%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF"
#     payload={}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     print(response.text)
#     url = f'https://sarthi.sonataindia.com/we_callback/{id}'  ## isko comment mat karna , webhook hai 
#     response = requests.request("POST", url)

    #thank you for putting date alert
#collection status alert
#payment full or partial alert
#full payment thanks alert
#partial payment how much alert

#after getting a DF with unique UserID and flows either running or to be started, we act on them
#if its running, 
    #if time elapsed (current time - update time) > 5 min, 
        #then mark as incomplete
#if status is none,
    #start flow, mark it as running
# print("Queueueueueu" , queue_df.to_dict('r'))
for flow in queue_df.to_dict('r'):
    print("ffffff",flow['flow_name'], flow['status'])
    if flow['status'] == 1:
        # if flow['update_time'] > (datetime.now() + timedelta(minutes=5)):
        if datetime.now() > (flow['update_time'] + timedelta(minutes=5)):
            # print('Status changing ......')
            url = f"https://sarthi.sonataindia.com/running_to_incomplete/{flow['id']}"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            # flow['status'] = 3
        else:
            pass 
    else:

        # if flow['update_time'] <= datetime.now() and flow['update_time'] > (datetime.now() - timedelta(minutes=5)):
            #send data
            #check flow type
        if flow['flow_name'] == 'Collection FollowUp':
            cfu_1(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'Collection Reminder':
            cfu_2(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'Collection Confirmation':
            cfu_3(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'Retention FollowUp':
            ret_1(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'Retention Reminder':
            ret_2(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'Retention Confirmation': 
            ret_3(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'WNAP_alert':
            WNAP_alert(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'WNAP_flow':
            print('idan')
            WNAP_flow(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'WNANP_flow':
            WNANP_flow(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'WNV_flow':
            WNV_flow(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])
        elif flow['flow_name'] == 'WNV_alert':
            WNV_alert(flow['id'],flow['contact_number'],flow['field_1'],flow['field_2'],flow['field_3'],flow['field_4'],flow['field_5'],flow['field_6'],flow['field_7'],flow['field_8'],flow['field_9'],flow['field_10'],flow['field_11'],flow['field_12'])






#collab with whatsapp callback function
#on proper reply from user and proper response to user, we update the queue's stage, update_time and response
#based on the stage we work our way out(basically replace the logic of whatsapp log with whatsapp queue, instead of latest log we choose running flow)

#for example:
#flow for CFU:
#trigger: sets queue entry along with all other variable details, status = "", stage = "", sends message when script runs over it, status = "running", stage = "bcd_alert"
#reply from user in button saying yes/no:
    #callback function acts up
        #finds out the running flow
            #sends relevant data and updates the running flow based on reply, eg reply is no
                #then flow gets updated, stage = 'ask_date'
#reply from user in text as the date:
    #callback function acts up
        #checks running flow's status
            #verifies the date is correctly sent
                #proceeds further and ends the flow with a message, status = "complete", stage = ""

