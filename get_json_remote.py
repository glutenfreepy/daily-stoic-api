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
        if key == "":
            db.put({"title": stoic_title})
            print(f"{stoic_title}\n\b")
        else:
            stoic_title = data.get(f"{key}", {}).get("title")
            print(type(key))
            key = key.replace(" ", "_")
            db.put({"title": stoic_title, "key": key})
            print(f"{key}\n{stoic_title}\n\b")
else:
    print(f'Bad Status Code: {response.status_code}')
