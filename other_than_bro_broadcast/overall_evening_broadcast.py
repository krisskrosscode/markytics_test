# imports
import json
import os
import warnings
from datetime import date, datetime, timedelta

import pandas as pd
import requests
from sqlalchemy import create_engine

warnings.filterwarnings("ignore")

MORNING_LEAD_LIST_ID = 214864
MORNING_BROADCAST_ID = 82319
EVENING_LEAD_LIST_ID = 214867
EVENING_BROADCAST_ID = 82321

## auth token
# from login import auth_token

# db information
user1 = "SFPL_Connect"
password = "$%n5bF33%X"
db = "Sonata_Connect"
server = "172.17.130.216"
engine = create_engine(
    f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server"
)


def get_authorization():
    """Get auth token"""
    username = os.environ["PAYMEE_SONATA_TATA_USERNAME"]
    password = os.environ["PAYMEE_SONATA_TATA_PASSWORD"]
    print(username, password)
    url = "https://api-smartflo.tatateleservices.com/v1/auth/login"

    payload = {"email": username, "password": password}
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None


auth_token = get_authorization()


def get_all_leads_in_leadlist():
    url = f"https://api-smartflo.tatateleservices.com/v1/broadcast/leads/{MORNING_LEAD_LIST_ID}"

    headers = {"accept": "application/json", "Authorization": auth_token}

    response = requests.get(url, headers=headers)

    # print(response.json())
    all_leadlist_contacts = {}

    for data in response.json():
        all_leadlist_contacts[data["field_0"]] = data["lead_id"]
    # print(all_leadlist_contacts)
    return all_leadlist_contacts





today_date = str(date.today())
today_date = datetime.strptime(today_date, "%Y-%m-%d").strftime("%Y-%m-%d")
sql_query = f""" SET NOCOUNT ON;EXEC [{db}].[dbo].[SP_UserHierarchy_Dynamic_07Jan23] @userid = 1;SET NOCOUNT OFF """
hierarchy_df = pd.read_sql_query(sql_query, engine)

bro_df = hierarchy_df[hierarchy_df["RoleId"] == 55][["UserID", "UserName"]]

bro_df.rename(
    columns={"UserID": "BRO_UserID", "UserName": "BRO_UserName"}, inplace=True
)


sql_query = f"""SET NOCOUNT ON;EXEC [{db}].[dbo].[SP_UserHierarchy_Dynamic_07Jan23] @userid = 1;SET NOCOUNT OFF"""
df = pd.read_sql_query(sql_query, engine)
df = df.replace(["Prayagraj Division", "Lucknow Division"], ["Prayagraj", "Lucknow"])

df = df.replace(["Prayagraj Division", "Lucknow Division"], ["Prayagraj", "Lucknow"])
# WE CREATE A NEW USER HIERARCHY TABLE
div_df = df[(df["RoleId"] == 34) & (df["RoleName"] == "DIVISION HEAD")][
    ["U_BUID", "UserID", "UserName", "buname"]
]
print(len(div_df))
div_df.rename(
    columns={
        "U_BUID": "Div_BUID",
        "buname": "DivName",
        "UserID": "Div_UserID",
        "UserName": "Div_UserName",
    },
    inplace=True,
)
reg_df = df[(df["RoleId"] == 35) & (df["RoleName"] == "REGION HEAD")][
    ["U_BUID", "UserID", "UserName", "buname", "ReportingBUId"]
]
print(len(reg_df))
reg_df.rename(
    columns={
        "U_BUID": "Region_BUID",
        "ReportingBUId": "Region_ReportingBUId",
        "buname": "RegionName",
        "UserID": "Region_UserID",
        "UserName": "Region_UserName",
    },
    inplace=True,
)
# hub_df = df[(df['RoleId']==44)&(df['RoleName']=='Credit Committee')][['U_BUID','UserID','UserName','buname','ReportingBUId']]
hub_df = df[
    (df["RoleId"].isin([36, 44, 42]))
    & (df["RoleName"].isin(["Credit Committee", "Credit Officer", "HUB HEAD"]))
][["U_BUID", "UserID", "UserName", "buname", "ReportingBUId", "RoleId"]]
# We will classify HUB,CRC,CRO on the basis of RID
hub_df.rename(
    columns={
        "U_BUID": "Hub_BUID",
        "ReportingBUId": "Hub_ReportingBUId",
        "buname": "HubName",
        "UserID": "Hub_UserID",
        "UserName": "Hub_UserName",
        "RoleId": "RID",
    },
    inplace=True,
)
bm_df = df[(df["RoleId"] == 13) & (df["RoleName"] == "Branch Manager")][
    ["U_BUID", "buname", "UserID", "UserName", "ReportingBUId"]
]
bm_df.rename(
    columns={
        "U_BUID": "BM_BUID",
        "ReportingBUId": "BM_ReportingBUId",
        "buname": "BranchName",
        "UserID": "BM_UserID",
        "UserName": "BM_UserName",
    },
    inplace=True,
)
bro_df = df[(df["RoleId"] == 55) & (df["RoleName"] == "BRO")][
    ["U_BUID", "UserID", "UserName", "buname"]
]
bro_df.rename(
    columns={
        "U_BUID": "BRO_BUID",
        "UserID": "BRO_UserID",
        "UserName": "BRO_UserName",
        "buname": "BRO_buname",
    },
    inplace=True,
)
M1 = pd.merge(
    bro_df, bm_df, left_on="BRO_BUID", right_on="BM_BUID", how="left"
).drop_duplicates(subset="BRO_UserID")
M2 = pd.merge(
    M1, hub_df, left_on="BM_ReportingBUId", right_on="Hub_BUID", how="left"
).drop_duplicates(subset="BRO_UserID")
M3 = pd.merge(
    M2, reg_df, left_on="Hub_ReportingBUId", right_on="Region_BUID", how="left"
).drop_duplicates(subset="BRO_UserID")
dF = pd.merge(
    M3, div_df, left_on="Region_ReportingBUId", right_on="Div_BUID", how="left"
).drop_duplicates(subset="BRO_UserID")



cols_to_fill = [
    "BM_BUID",
    "BM_UserID",
    "BM_ReportingBUId",
    "Hub_BUID",
    "Hub_UserID",
    "Hub_ReportingBUId",
    "RID",
    "Region_BUID",
    "Region_UserID",
    "Region_ReportingBUId",
    "Div_BUID",
    "Div_UserID",
]
dF[cols_to_fill] = dF[cols_to_fill].fillna(0).astype("int", errors="ignore")


# task count
today_date = datetime.strptime(str(date.today()), "%Y-%m-%d").strftime("%Y-%m-%d")
sql_query = f""" SET NOCOUNT ON;EXEC [{db}].[dbo].[SP_UserHierarchy_Dynamic_07Jan23] @userid = 1;SET NOCOUNT OFF """
hierarchy_df = pd.read_sql_query(sql_query, engine)
hierarchy_df = hierarchy_df[hierarchy_df["RoleId"] == 55]
hierarchy_df = hierarchy_df[["UserID", "UserName"]]
userid_tuple = tuple(hierarchy_df["UserID"].unique().tolist())
sql_query = f""" SELECT CallingNumber,UserID FROM Sonata_Connect.dbo.accounts_calling_number_list
    WHERE UserID in {userid_tuple} """
contact_df = pd.read_sql_query(sql_query, engine)
main_df = pd.merge(hierarchy_df, contact_df, on="UserID", how="right")
# sql_query = f""" SELECT TOP 10 assigned_to,status,deadline_date FROM Sonata_Connect.dbo.accounts_task_details
#     WHERE assigned_to in {userid_tuple} and deadline_date = {today_date} """
sql_query = f""" SELECT assigned_to,status,deadline_date,category FROM Sonata_Connect.dbo.accounts_task_details
    WHERE deadline_date = '{today_date}' and category in ('3','5','7','10')"""

task_df = pd.read_sql_query(sql_query, engine)
task_df = task_df[(task_df['status'] == 'Completed')]

pending_task_df = task_df.groupby("assigned_to")["deadline_date"].count().reset_index()
pending_task_df = pending_task_df.rename(columns={"deadline_date": "Pending_Count"})

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
main_df = pd.merge(main_df,pending_task_df,left_on='UserID',right_on='assigned_to',how='left')

main_df = pd.merge(main_df,completed_task_df,left_on='UserID',right_on='assigned_to',how='left')
# main_df_incomplete = pd.merge(main_df,completed_task_df,left_on='UserID',right_on='assigned_to',how='left')
# print(len(main_df))
main_df = pd.merge(main_df,collection2_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,proposal2_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,retention2_task_df,left_on='UserID',right_on='assigned_to',how='left')
main_df = pd.merge(main_df,wrong_number2_task_df,left_on='UserID',right_on='assigned_to',how='left')

main_df = main_df.drop(columns=['assigned_to_y', 'assigned_to_x'], axis=1).dropna(subset=['UserID']).fillna(0).reset_index(drop=True)

main_df['Pending_Count'] = main_df['Pending_Count'].astype(int, errors='ignore')
main_df['Completed_Count'] = main_df['Completed_Count'].astype(int, errors='ignore')

main_df['collection2_count'] = main_df['collection2_count'].astype(int, errors='ignore')
main_df['proposal2_count'] = main_df['proposal2_count'].astype(int, errors='ignore')
main_df['retention2_count'] = main_df['retention2_count'].astype(int, errors='ignore')
main_df['wrong_number2_count'] = main_df['wrong_number2_count'].astype(int, errors='ignore')

main_df['UserID'] = main_df['UserID'].astype(int, errors='ignore')
main_df['UserName'] = main_df['UserName'].apply(lambda x : x.title())


# main_df = main_df.drop("assigned_to", axis=1)





main_df.rename(
    columns={"UserID": "BRO_UserID", "UserName": "BRO_UserName"}, inplace=True
)
main_df


# dF[dF["BRO_UserID"] == 31810]


main_df = (
    pd.merge(
        left=main_df, right=dF, left_on="BRO_UserID", right_on="BRO_UserID", how="left"
    )
    .drop("BRO_UserName_y", axis=1)
    .rename(columns={"BRO_UserName_x": "BRO_UserName"})
)


brogroup_df = (
    main_df.groupby("BRO_UserID")
    .agg(
        {
            "BRO_UserName": "first",
            "Pending_Count": "sum",
            "Completed_Count": "sum",
            "collection2_count": "sum",
            "proposal2_count": "sum",
            "retention2_count": "sum",
            "wrong_number2_count": "sum",
        }
    )
    .reset_index()
    .rename(columns={"BRO_UserID": "UserID", "BRO_UserName": "UserName"})
)

userid_tuple = tuple(brogroup_df["UserID"].unique().tolist())
sql_query = f""" SELECT CallingNumber,UserID FROM Sonata_Connect.dbo.accounts_calling_number_list
    WHERE UserID in {userid_tuple} """
contact_df = pd.read_sql_query(sql_query, engine)
brogroup_df = pd.merge(brogroup_df, contact_df, on="UserID", how="left").dropna()
brogroup_df


## Creating groups based on roles


bmgroup_df = (
    main_df.groupby("BM_UserID")
    .agg(
        {
            "BM_UserName": "first",
            "Pending_Count": "sum",
            "Completed_Count": "sum",
            "collection2_count": "sum",
            "proposal2_count": "sum",
            "retention2_count": "sum",
            "wrong_number2_count": "sum",
        }
    )
    .reset_index()
    .rename(columns={"BM_UserID": "UserID", "BM_UserName": "UserName"})
)

userid_tuple = tuple(bmgroup_df["UserID"].unique().tolist())
sql_query = f""" SELECT CallingNumber,UserID FROM Sonata_Connect.dbo.accounts_calling_number_list
    WHERE UserID in {userid_tuple} """
contact_df = pd.read_sql_query(sql_query, engine)
bmgroup_df = pd.merge(bmgroup_df, contact_df, on="UserID", how="left").dropna()
bmgroup_df





hubgroup_df = (
    main_df.groupby("Hub_UserID")
    .agg(
        {
            "Hub_UserName": "first",
            "Pending_Count": "sum",
            "Completed_Count": "sum",
            "collection2_count": "sum",
            "proposal2_count": "sum",
            "retention2_count": "sum",
            "wrong_number2_count": "sum",
        }
    )
    .reset_index()
    .rename(columns={"Hub_UserID": "UserID", "Hub_UserName": "UserName"})
)

userid_tuple = tuple(hubgroup_df["UserID"].unique().tolist())
sql_query = f""" SELECT CallingNumber,UserID FROM Sonata_Connect.dbo.accounts_calling_number_list
    WHERE UserID in {userid_tuple} """
contact_df = pd.read_sql_query(sql_query, engine)
hubgroup_df = pd.merge(hubgroup_df, contact_df, on="UserID", how="left").dropna()
hubgroup_df


regiongroup_df = (
    main_df.groupby("Region_UserID")
    .agg(
        {
            "Region_UserName": "first",
            "Pending_Count": "sum",
            "Completed_Count": "sum",
            "collection2_count": "sum",
            "proposal2_count": "sum",
            "retention2_count": "sum",
            "wrong_number2_count": "sum",
        }
    )
    .reset_index()
    .rename(columns={"Region_UserID": "UserID", "Region_UserName": "UserName"})
)

userid_tuple = tuple(regiongroup_df["UserID"].unique().tolist())
sql_query = f""" SELECT CallingNumber,UserID FROM Sonata_Connect.dbo.accounts_calling_number_list
    WHERE UserID in {userid_tuple} """
contact_df = pd.read_sql_query(sql_query, engine)
regiongroup_df = pd.merge(regiongroup_df, contact_df, on="UserID", how="left").dropna()
regiongroup_df


divgroup_df = (
    main_df.groupby("Div_UserID")
    .agg(
        {
            "Div_UserName": "first",
            "Pending_Count": "sum",
            "Completed_Count": "sum",
            "collection2_count": "sum",
            "proposal2_count": "sum",
            "retention2_count": "sum",
            "wrong_number2_count": "sum",
        }
    )
    .reset_index()
    .rename(columns={"Div_UserID": "UserID", "Div_UserName": "UserName"})
)





userid_tuple = tuple(divgroup_df["UserID"].unique().tolist())
sql_query = f""" SELECT CallingNumber,UserID FROM Sonata_Connect.dbo.accounts_calling_number_list
    WHERE UserID in {userid_tuple} """
contact_df = pd.read_sql_query(sql_query, engine)
divgroup_df = pd.merge(divgroup_df, contact_df, on="UserID", how="left").dropna()
divgroup_df


all_df = pd.concat(
    [brogroup_df, bmgroup_df, hubgroup_df, regiongroup_df, divgroup_df], axis=0
).reset_index(drop=True)

print(all_df.head())
print("shape of all_df", all_df.shape)


## inserting data into broadcast/leadlist


## stop broadcast -> harshal
stop_evening_broadcast_url = (
    f"https://api-smartflo.tatateleservices.com/v1/broadcast/end/{EVENING_BROADCAST_ID}"
)
stop_morning_broadcast_url = (
    f"https://api-smartflo.tatateleservices.com/v1/broadcast/end/{MORNING_BROADCAST_ID}"
)

headers = {"accept": "application/json", "Authorization": auth_token}
stop_morning_broadcast_response = requests.get(
    stop_morning_broadcast_url, headers=headers
)
stop_evening_broadcast_response = requests.get(
    stop_evening_broadcast_url, headers=headers
)
print(stop_morning_broadcast_response.text)
print(stop_evening_broadcast_response.text)



## updating lead lists with new values 
pending_count_hindi_text = ' , कार्य थे '
completed_count_hindi_text = ', पूरे हुए ।'
collection_count_hindi_text = ' कलेक्शन संबंधी कार्य '
proposal_count_hindi_text = ' प्रपोजल संबंधी कार्य '
retention_count_hindi_text = ' रिटेंशन संबंधी कार्य '
wrong_number_count_hindi_text = ' गलत फोन नंबर सुधार संबंधी कार्य हैं । '


leadlist = get_all_leads_in_leadlist()
print(all_df.shape)
print('\n\n\n\n\n', all_df.head())

for data in all_df.head(2).to_dict('r'):
    """ Updating lead list"""

    if data['Completed_Count'] == 0:
        print('task complete karo bhaiyon....')
        field_5_string = 'आपने आज ,, कोई कार्य ,,  पूर्ण नहीं किया।।।। कृपया अपने कार्य पूर्ण करें।'

    else:
        field_5_string = f"।।आपके पास।।।।,"  ## stores all counts as formatted string

        pending_count = data['Pending_Count']
        field_5_string += ((str(pending_count) + pending_count_hindi_text + 'और') if pending_count != 0 else '')

        completed_count = data['Completed_Count']
        field_5_string += ((str(completed_count) + completed_count_hindi_text + '। जिनमें से ,' ) if pending_count != 0 else '')

        collection_count = data['collection2_count']
        field_5_string += ((str(collection_count) + collection_count_hindi_text  ) if collection_count != 0 else '')

        proposal_count = data['proposal2_count']
        field_5_string += ((str(proposal_count) + proposal_count_hindi_text) if proposal_count != 0 else '')

        retention_count = data['retention2_count']
        field_5_string += ((str(retention_count) + retention_count_hindi_text) if retention_count != 0 else '')


        wrong_number_count = data['wrong_number2_count']
        field_5_string += ((str(wrong_number_count) + wrong_number_count_hindi_text) if wrong_number_count != 0 else '')


    if ('+91'+ data['CallingNumber']) in leadlist.keys():
        print('leadlist update ho rahi hai.... ')
        # data['status'] = '1'
        # update_lead(leadlist['+91' + '9162841833'])
        # print(data['CallingNumber'])
        lead_id = leadlist['+91' + data['CallingNumber']]  #leadlist['+91' + '9162841833']
        url = f"https://api-smartflo.tatateleservices.com/v1/broadcast/lead/{lead_id}" ## update lead api call

        headers = {
            "accept": "application/json",
            "Authorization": auth_token,
            "content-type": "application/json"
        }
        payload = {
            'dial_status' : '1',
            'field_1': data['UserName'],
            'field_5': field_5_string
        }
        # response = requests.put(url, headers=headers, json= payload)
        # print(response.text)

    else:
        print('leadlist me leads add ho rahe hain.... ')
        url = f"https://api-smartflo.tatateleservices.com/v1/broadcast/lead/{EVENING_LEAD_LIST_ID}"

        payload = json.dumps({
        # "field_0": data['CallingNumber'],
        "field_0": '9162841833',
        "field_1": data['UserName'],
        "field_5": field_5_string,

        })
        headers = {
        'Accept': 'application/json',
        'Authorization': auth_token,
        'Content-Type': 'application/json'
        }

        # response = requests.request("POST", url, headers=headers, data=payload)

        # print(response.text)
        


