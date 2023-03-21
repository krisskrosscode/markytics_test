import requests

url = "https://api-smartflo.tatateleservices.com/v1/broadcast/lead/214109"

payload = {
    "field_0": "9162841833",
    "field_1": "Harshal P"
}
headers = {
    "accept": "application/json",
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2xvdWRwaG9uZS50YXRhdGVsZXNlcnZpY2VzLmNvbVwvYXBpXC92MVwvYXV0aFwvcmVmcmVzaCIsImlhdCI6MTY3ODc3MzkxOSwiZXhwIjoxNjc4Nzc3NTgxLCJuYmYiOjE2Nzg3NzM5ODEsImp0aSI6ImF0QUxCS0NFeFljQ3o2WXciLCJzdWIiOjMzNjM5OX0.2AWCzlSUzsJB_1ucPSvj1-Bwpt1hSBOGFXFM5z67PnI",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text) 

