# Get the remote json file with the Daily Stoic data
# and load it into your Deta Micro's database

import requests
from decouple import config
from deta import Deta

DETA_PROJECT_KEY = config('DETA_PROJECT_KEY')
DB_NAME = config('DETA_DB_NAME')
URL = "https://raw.githubusercontent.com/IshanMi/Stoicbot/master/pdf_parsing/Stoic_log.json"

deta = Deta(DETA_PROJECT_KEY)
db = deta.Base(DB_NAME)

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    for key, val in data.items():
        # check json file for empty key entries and if found,
        # only enter the title into the deta db.  deta will
        # enter a key automically since one was not provided
        if key == "":
            db.put({"title": stoic_title})
        else:
            stoic_title = data.get(f"{key}", {}).get("title")
            key = key.replace(" ", "_")
            db.put({"title": stoic_title, "key": key})
else:
    print(f'Bad Status Code: {response.status_code}')
