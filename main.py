from http.client import HTTPException

from fastapi import FastAPI
from fastapi.openapi.utils import status_code_ranges
from pydantic import BaseModel
from typing import List
app = FastAPI()

@app.get("/ping")
def ping():
    return "pong"

class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristic

Cars_db: List[Car]:[]

@app.get("/cars")
def get_cars():
    return  List(Cars_db.values())

@app.get("/cars/{id}")
def get_car_id(id: str):
    if id not in Cars_db:
        raise HTTPException(status_code=404, detail=f"Car with ID '{id}' was not found.")
    return Cars_db[id]