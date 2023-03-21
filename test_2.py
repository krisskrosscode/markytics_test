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

today_date = str(date.today())
today_date = datetime.strptime(today_date, '%Y-%m-%d').strftime('%Y-%m-%d')
sql_query = f""" SET NOCOUNT ON;EXEC [{db}].[dbo].[SP_UserHierarchy_Dynamic_07Jan23] @userid = 1;SET NOCOUNT OFF """
hierarchy_df=pd.read_sql_query(sql_query,engine)
hierarchy_df = hierarchy_df[hierarchy_df['RoleId']==55]
hierarchy_df = hierarchy_df[['UserID','UserName']]
userid_tuple = tuple(hierarchy_df['UserID'].unique().tolist())
sql_query = f""" SELECT CallingNumber,UserID FROM Sonata_Connect.dbo.accounts_calling_number_list
    WHERE UserID in {userid_tuple} """
contact_df = pd.read_sql_query(sql_query,engine)
main_df = pd.merge(hierarchy_df,contact_df,on='UserID',how='right')
# sql_query = f""" SELECT TOP 10 assigned_to,status,deadline_date FROM Sonata_Connect.dbo.accounts_task_details
#     WHERE assigned_to in {userid_tuple} and deadline_date = {today_date} """
sql_query = f""" SELECT assigned_to,status,deadline_date,category FROM Sonata_Connect.dbo.accounts_task_details
    WHERE deadline_date = '{today_date}' and category in ('3','5','7','10')"""

# '2023-03-14'
task_df = pd.read_sql_query(sql_query,engine)
task_df = task_df[(task_df['status'] == 'Pending')|(task_df['status'] == 'Re-Schedule')]
pending_task_df = task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
pending_task_df = pending_task_df.rename(columns={'deadline_date':'Pending_Count'})

print("Length of pending taks : ", len(pending_task_df))

collection_task_df = task_df[task_df['category']=='3']
collection_task_df = collection_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
collection_task_df = collection_task_df.rename(columns={'deadline_date':'collection_count'})

proposal_task_df = task_df[task_df['category']=='5']
proposal_task_df = proposal_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
proposal_task_df = proposal_task_df.rename(columns={'deadline_date':'proposal_count'})

retention_task_df = task_df[task_df['category']=='7']
retention_task_df = retention_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
retention_task_df = retention_task_df.rename(columns={'deadline_date':'retention_count'})

wrong_number_task_df = task_df[task_df['category']=='10']
wrong_number_task_df = wrong_number_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
wrong_number_task_df = wrong_number_task_df.rename(columns={'deadline_date':'wrong_number_count'})

task_df = task_df[(task_df['status'] == 'Completed')]
completed_task_df = task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
completed_task_df = completed_task_df.rename(columns={'deadline_date':'Completed_Count'})

collection2_task_df = task_df[task_df['category']=='3']
collection2_task_df = collection2_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
collection2_task_df = collection2_task_df.rename(columns={'deadline_date':'collection2_count'})

proposal2_task_df = task_df[task_df['category']=='5']
proposal2_task_df = proposal2_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
proposal2_task_df = proposal2_task_df.rename(columns={'deadline_date':'proposal2_count'})

retention2_task_df = task_df[task_df['category']=='7']
retention2_task_df = retention2_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
retention2_task_df = retention2_task_df.rename(columns={'deadline_date':'retention2_count'})

wrong_number2_task_df = task_df[task_df['category']=='10']
wrong_number2_task_df = wrong_number2_task_df.groupby('assigned_to')['deadline_date'].count().reset_index()
wrong_number2_task_df = wrong_number2_task_df.rename(columns={'deadline_date':'wrong_number2_count'})
# print(pending_task_df,completed_task_df)
# main_df = pd.merge(main_df,pending_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,pending_task_df,left_on='UserID',right_on='assigned_to',how='right')
main_df = pd.merge(main_df,collection_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,proposal_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,retention_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,wrong_number_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,completed_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,collection2_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,proposal2_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,retention2_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,wrong_number2_task_df,left_on='UserID',right_on='assigned_to',how='left')


# main_df = main_df.drop(['assigned_to','assigned_to_x','assigned_to_y'], axis=1).fillna(0)

main_df = main_df.drop(columns=['assigned_to_y', 'assigned_to_x'], axis=1).dropna(subset=['UserID']).fillna(0).reset_index(drop=True)

main_df['collection_count'] = main_df['collection_count'].astype(int, errors='ignore')
main_df['proposal_count'] = main_df['proposal_count'].astype(int, errors='ignore')
main_df['retention_count'] = main_df['retention_count'].astype(int, errors='ignore')
main_df['wrong_number_count'] = main_df['wrong_number_count'].astype(int, errors='ignore')

# main_df['Completed_Count'] = main_df['wrong_number_count'].astype(int, errors='ignore')
main_df['Completed_Count'] = main_df['Completed_Count'].astype(int, errors='ignore')

main_df['collection2_count'] = main_df['collection2_count'].astype(int, errors='ignore')
main_df['proposal2_count'] = main_df['proposal2_count'].astype(int, errors='ignore')
main_df['retention2_count'] = main_df['retention2_count'].astype(int, errors='ignore')
main_df['wrong_number2_count'] = main_df['wrong_number2_count'].astype(int, errors='ignore')

main_df['UserID'] = main_df['UserID'].astype(int, errors='ignore')
main_df['UserName'] = main_df['UserName'].apply(lambda x : x.title())

# main_df = main_df[main_df['collection_count']>0]
# main_df = main_df[main_df['retention_count']>0]
# main_df = main_df.sort_values(by='Pending_Count')


# print(main_df.dtypes)

print("Main df len" , len(main_df))
# print(main_df[['CallingNumber', 'UserName']])



## stop broadcast -> harshal
stop_first_broadcast_url = "https://api-smartflo.tatateleservices.com/v1/broadcast/end/82183"
stop_second_broadcast_url = "https://api-smartflo.tatateleservices.com/v1/broadcast/end/82184"
stop_third_broadcast_url = "https://api-smartflo.tatateleservices.com/v1/broadcast/end/82185"
headers = {
    "accept": "application/json",
    "Authorization": auth_token
}
stop_first_broadcast_response = requests.get(stop_first_broadcast_url, headers=headers)
print(stop_first_broadcast_response.text)

stop_second_broadcast_response = requests.get(stop_second_broadcast_url, headers=headers)
print(stop_second_broadcast_response.text)

stop_third_broadcast_response = requests.get(stop_third_broadcast_url, headers=headers)
print(stop_third_broadcast_response.text)


## Splitting into 3 dataframes
split_window = len(main_df)//3
main_df_1 = main_df.iloc[0:split_window, :]
main_df_2 = main_df.iloc[split_window: 2*split_window, :]
main_df_3 = main_df.iloc[2*split_window:]

print(len(main_df), len(main_df_1), len(main_df_2), len(main_df_3))




## updating lead lists with new values 

collection_count_hindi_text = 'कलेक्शन संबंधी कार्य हैं । '
proposal_count_hindi_text = 'प्रपोजल संबंधी कार्य हैं । '
retention_count_hindi_text = 'रिटेंशन संबंधी कार्य हैं । '
wrong_number_count_hindi_text = 'गलत फोन नंबर सुधार संबंधी कार्य हैं । '

## to lead list 1 
for data in main_df_1.head(2).to_dict('r'):
    """ Updating lead list 1 """

    url = "https://api-smartflo.tatateleservices.com/v1/broadcast/lead/214215"

    payload = json.dumps({
    "field_0": data['CallingNumber'],
    "field_1": data['UserName'],
    "field_5": str(data['Pending_Count']),
    "field_6": (str(data['collection_count']) + collection_count_hindi_text) if data['collection_count'] != 0 else '',
    "field_7": (str(data['proposal_count']) + proposal_count_hindi_text) if data['proposal_count'] != 0 else '',
    "field_8": (str(data['retention_count']) + retention_count_hindi_text) if data['retention_count'] != 0 else '',
    "field_9": (str(data['wrong_number_count']) + wrong_number_count_hindi_text if data['wrong_number_count'] != 0 else '' ),

    })
    headers = {
    'Accept': 'application/json',
    'Authorization': auth_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# # to lead list 2
# for data in main_df_2.to_dict('r'):
#     """ Updating lead list 2 """

#     url = "https://api-smartflo.tatateleservices.com/v1/broadcast/lead/214216"

#     payload = json.dumps({
#     "field_0": data['CallingNumber'],
#     "field_1": data['UserName'],
#     "field_5": str(data['Pending_Count']),
#     "field_6": (str(data['collection_count']) + collection_count_hindi_text) if data['collection_count'] != 0 else '',
#     "field_7": (str(data['proposal_count']) + proposal_count_hindi_text) if data['proposal_count'] != 0 else '',
#     "field_8": (str(data['retention_count']) + retention_count_hindi_text) if data['retention_count'] != 0 else '',
#     "field_9": (str(data['wrong_number_count']) + wrong_number_count_hindi_text if data['wrong_number_count'] != 0 else '' ),

#     })
#     headers = {
#     'Accept': 'application/json',
#     'Authorization': auth_token,
#     'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)


# # to lead list 3
# for data in main_df_3.to_dict('r'):
#     """ Updating lead list 3 """
#     url = "https://api-smartflo.tatateleservices.com/v1/broadcast/lead/214217"
    
#     payload = json.dumps({
#     "field_0": data['CallingNumber'],
#     "field_1": data['UserName'],
#     "field_5": str(data['Pending_Count']),
#     "field_6": (str(data['collection_count']) + collection_count_hindi_text) if data['collection_count'] != 0 else '',
#     "field_7": (str(data['proposal_count']) + proposal_count_hindi_text) if data['proposal_count'] != 0 else '',
#     "field_8": (str(data['retention_count']) + retention_count_hindi_text) if data['retention_count'] != 0 else '',
#     "field_9": (str(data['wrong_number_count']) + wrong_number_count_hindi_text if data['wrong_number_count'] != 0 else '' ),

#     })
#     headers = {
#     'Accept': 'application/json',
#     'Authorization': auth_token,
#     'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)



