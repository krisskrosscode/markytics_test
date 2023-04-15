import os 
from sqlalchemy import create_engine
import pandas as pd

user1 = os.environ['PAYMEE_SONTATA_DB_USER']
password = os.environ['PAYMEE_SONTATA_DB_PASSWORD']
db = "Sonata_Connect"
server = "172.17.130.216"   

engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")

sql_query = f"""SET NOCOUNT ON;SELECT task_id, task_description, status, priority, assigned_to, deadline_date, category, review, feedback FROM [{db}].[dbo].accounts_task_details;SET NOCOUNT OFF"""
all_tasks_df=pd.read_sql_query(sql_query,engine)


sql_query = f"""SET NOCOUNT ON;EXEC [{db}].[dbo].[SP_UserHierarchy_Dynamic_07Jan23] @userid = 6892;SET NOCOUNT OFF"""
df=pd.read_sql_query(sql_query,engine)

#WE CREATE A NEW USER HIERARCHY TABLE
div_df = df[(df['RoleId']==34)&(df['RoleName']=='DIVISION HEAD')][['U_BUID','UserID','UserName','buname']]
div_df.rename(columns={'U_BUID':'Div_BUID','buname':'DivName','UserID':'Div_UserID','UserName':'Div_UserName'}, inplace=True)
reg_df = df[(df['RoleId']==35)&(df['RoleName']=='REGION HEAD')][['U_BUID','UserID','UserName','buname','ReportingBUId']]
reg_df.rename(columns={'U_BUID':'Region_BUID','ReportingBUId':'Region_ReportingBUId','buname':'RegionName','UserID':'Region_UserID','UserName':'Region_UserName'}, inplace=True)
hub_df = df[(df['RoleId']==36)&(df['RoleName']=='HUB HEAD')][['U_BUID','UserID','UserName','buname','ReportingBUId']]
hub_df.rename(columns={'U_BUID':'Hub_BUID','ReportingBUId':'Hub_ReportingBUId','buname':'HubName','UserID':'Hub_UserID','UserName':'Hub_UserName'}, inplace=True)
bm_df = df[(df['RoleId']==13)&(df['RoleName']=='Branch Manager')][['U_BUID','buname','UserID','UserName','ReportingBUId']]
bm_df.rename(columns={'U_BUID':'BM_BUID','ReportingBUId':'BM_ReportingBUId','buname':'BranchName','UserID':'BM_UserID','UserName':'BM_UserName'}, inplace=True)
bro_df = df[(df['RoleId']==55)&(df['RoleName']=='BRO')][['U_BUID','UserID','UserName']]
bro_df.rename(columns={'U_BUID':'BRO_BUID','UserID':'BRO_UserID','UserName':'BRO_UserName'}, inplace=True)
M1 = pd.merge(bro_df,bm_df,left_on='BRO_BUID',right_on='BM_BUID',how='left').drop_duplicates(subset='BRO_UserID')
M2 = pd.merge(M1,hub_df,left_on='BM_ReportingBUId',right_on='Hub_BUID',how='left').drop_duplicates(subset='BRO_UserID')
M3 = pd.merge(M2,reg_df,left_on='Hub_ReportingBUId',right_on='Region_BUID',how='left').drop_duplicates(subset='BRO_UserID')
dF = pd.merge(M3,div_df,left_on='Region_ReportingBUId',right_on='Div_BUID',how='left').drop_duplicates(subset='BRO_UserID')

# dF.to_csv('dF.csv')

# all_tasks_df.to_csv('all_tasks.csv')

reqdf = pd.merge(all_tasks_df, df, how='left', left_on='assigned_to', right_on='UserID')
reqdf.to_csv('testcsv.csv')