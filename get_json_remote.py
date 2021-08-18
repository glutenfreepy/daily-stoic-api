import requests
import time
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
    for key in data:
        stoic_title = data.get(f"{key}", {}).get("title")
        db.put({"title": stoic_title, "key": key})
        time.sleep(1)
else:
    print(f'Bad Status Code: {response.status_code}')
