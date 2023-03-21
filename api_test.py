import requests

url = "https://api-smartflo.tatateleservices.com/v1/broadcast/82124"

headers = {
    "accept": "application/json",
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2xvdWRwaG9uZS50YXRhdGVsZXNlcnZpY2VzLmNvbVwvYXBpXC92MVwvYXV0aFwvbG9naW4iLCJpYXQiOjE2Nzg3NjgyMDMsImV4cCI6MTY3ODc3MTgwMywibmJmIjoxNjc4NzY4MjAzLCJqdGkiOiI2cENJM1I1S1lYUDk2cE9kIiwic3ViIjozMzYzOTl9.hk84q3BLfm5olwJ0oNh-APSMZbpYnpEAH2E89DYYoJE"
}

response = requests.get(url, headers=headers)

print(response.text)