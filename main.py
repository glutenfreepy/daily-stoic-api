from decouple import config
from deta import Deta
from fastapi import FastAPI, HTTPException

DETA_PROJECT_KEY = config('DETA_PROJECT_KEY')
DB_NAME = config('DETA_DB_NAME')

deta = Deta(DETA_PROJECT_KEY)
db = deta.Base(DB_NAME)

app = FastAPI()


@app.get("/thedailystoic/", status_code=200)
def get_stoics():
    response = db.fetch()
    all_stoics = response.items
    return all_stoics


@app.get("/thedailystoic/{key}", status_code=200)
def get_stoic(key: str):
    dailystoic = db.get(key)
    if dailystoic is None:
        raise HTTPException(status_code=404, detail="Not found")
    return dailystoic
