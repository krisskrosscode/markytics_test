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




def start_morning_broadcast(authorization_token, morning_broadcast_id):
    url = f"https://api-smartflo.tatateleservices.com/v1/broadcast/start/{morning_broadcast_id}"

    headers = {
        "accept": "application/json",
        "Authorization": authorization_token
    }

    start_broadcast_response = requests.get(url, headers=headers)

    print(start_broadcast_response.text)



auth_token = get_authorization()

start_morning_broadcast(authorization_token=auth_token, morning_broadcast_id=MORNING_BROADCAST_ID)

