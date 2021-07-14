from decouple import config

from deta import Deta
from fastapi import FastAPI

DETA_PROJECT_KEY = config('DETA_PROJECT_KEY')
DB_NAME = config('DB_NAME')

deta = Deta(DETA_PROJECT_KEY)
db = deta.Base('DB_NAME')
app = FastAPI()


@app.get("/", status_code=200)
def get_hello():
    return {"Hello": "World"}


@app.get("/dailystoic/<key>")
def get_stoic_of_the_day(key):
    dailystoic = dailystoics.get(key)
    return dailystoic if dailystoic else jsonify({"error": "Not found"}, 404)
