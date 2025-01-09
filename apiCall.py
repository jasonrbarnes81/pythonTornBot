from urllib import response
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
tornKey = os.getenv("TORN_KEY")

def Items():
    response = requests.get("https://api.torn.com/torn/?selections=items&key="+tornKey)
    return json.loads(response.content)

def Travel():
    res = requests.get("https://yata.yt/api/v1/travel/export/")
    return json.loads(res.content)

