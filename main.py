from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from prisma import Prisma
import numpy as np
import pandas as pd

app = FastAPI()
db = Prisma()

# Pydantic Model for Data Validation
class StockData(BaseModel):
    datetime: str
    open: float
    high: float
    low: float
    close: float
    volume: int

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

# ✅ GET all stock data
@app.get("/data")
async def get_stock_data():
    records = await db.stockdata.find_many()
    return records

# ✅ POST new stock data
@app.post("/data")
async def insert_stock_data(data: StockData):
    try:
        new_record = await db.stockdata.create(data=data.dict())
        return {"message": "Data inserted successfully", "data": new_record}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
