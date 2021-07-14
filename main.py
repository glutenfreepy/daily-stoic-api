from decouple import config

from deta import Deta
from fastapi import FastAPI, HTTPException

DETA_PROJECT_KEY = config('DETA_PROJECT_KEY')
DB_NAME = config('DETA_DB_NAME')

dbkey = DETA_PROJECT_KEY
dbname = DB_NAME

deta = Deta(dbkey)
db = deta.Base(dbname)

app = FastAPI()


@app.get("/thedailystoic/{key}", status_code=200)
def get_stoic(key: str):
    print(key)
    print(dbkey)
    print(dbname)
    dailystoic = db.get(key)
    if dailystoic is None:
        raise HTTPException(status_code=404, detail="Not found")
    return dailystoic
