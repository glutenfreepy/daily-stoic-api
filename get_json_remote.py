import re
import requests
from decouple import config
from deta import Deta

DETA_PROJECT_KEY = config('DETA_PROJECT_KEY')
DB_NAME = config('DETA_DB_NAME')

deta = Deta(DETA_PROJECT_KEY)
db = deta.Base(DB_NAME)

URL = "https://raw.githubusercontent.com/IshanMi/Stoicbot/master/pdf_parsing/Stoic_log.json"
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    for key, val in data.items():
        stoic_title = data.get(f"{key}", {}).get("title")
        key = key.replace(" ", "_")
        # print(f"{key}\n{stoic_title}\n\b")
        db.put({"title": stoic_title, "key": key})
else:
    print(f'Bad Status Code: {response.status_code}')
