import requests

url = "https://api-smartflo.tatateleservices.com/v1/auth/refresh"

headers = {
    "accept": "application/json",
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2xvdWRwaG9uZS50YXRhdGVsZXNlcnZpY2VzLmNvbVwvYXBpXC92MVwvYXV0aFwvbG9naW4iLCJpYXQiOjE2Nzg3NzM5MTksImV4cCI6MTY3ODc3NzUxOSwibmJmIjoxNjc4NzczOTE5LCJqdGkiOiJXVGM4eWhNd25ScUVnVmoyIiwic3ViIjozMzYzOTl9.d339KmZG-csa1pTaWehKETazQe6R6efESLUV3HywuAw"
}

response = requests.post(url, headers=headers)

print(response.text)