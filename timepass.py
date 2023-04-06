from datetime import datetime, date, timedelta
import os
from sqlalchemy import create_engine
import pandas as pd
# print(date.today())
# print(datetime.now().date())

# print(datetime.strptime(datetime.now().time().strftime('%H:%M:%S'), '%H:%M:%S'))

# b = date.today()
# a =(datetime.now() - timedelta(hours=1)).time().strftime('%H:%M')

# print(a, b)

# user1 = os.environ['PAYMEE_SONTATA_DB_USER']
# password = os.environ['PAYMEE_SONTATA_DB_PASSWORD']
# db = "Sonata_Connect"
# server = "172.17.130.216"
# engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")
# sql_query = f""" UPDATE Sonata_Connect.dbo.WhatsAppQueue SET field_5 = '2023-04-13' where id IN (2939) """
# with engine.connect() as con:
#     con.execute(sql_query)


# user1 = os.environ['PAYMEE_SONTATA_DB_USER']
# password = os.environ['PAYMEE_SONTATA_DB_PASSWORD']
# db = "Sonata_Connect"
# server = "172.17.130.216"
# engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")
# sql_query = f""" UPDATE Sonata_Connect.dbo.WhatsAppQueue SET field_6 = {str(tym)} where id IN ({int(queue_running_inst.field_7)}, {int(queue_running_inst.field_8)}) """
# with engine.connect() as con:
#     con.execute(sql_query)
# from datetime import datetime

# datetime_str = '23-05-22 13:55:26'

# datetime_object = datetime.strptime(datetime_str, '%y-%m-%d %H:%M:%S')

# print(type(datetime_object))
# print(datetime_object)  # printed in default format

# udate = '2023-05-22'.split('-')
# tym = '2300'
# year = int(udate[0])
# month = int(udate[1])
# day = int(udate[2])
# hours = int(tym[:2])
# minutes = int(tym[2:])
# updated_datetime = datetime(year=year, month=month, day=day, hour= hours, minute=minutes)

# # print((updated_datetime.strftime("%H:%M")))

# tym = updated_datetime.time()
# print(str(updated_datetime.date()))


user1 = os.environ['PAYMEE_SONTATA_DB_USER']
password = os.environ['PAYMEE_SONTATA_DB_PASSWORD']
db = "Sonata_Connect_Test"
server = "172.17.130.216"
engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")
sql_query = f""" SELECT * from Sonata_Connect.dbo.WhatsAppQueue """
dg=pd.read_sql_query(sql_query,engine)
print(dg.head(1))

