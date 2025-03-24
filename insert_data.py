import pandas as pd
import asyncio
from prisma import Prisma

# Load Excel file
file_path = "/Users/sanchitkumar/Desktop/HINDALCO_1D.xlsx"
df = pd.read_excel(file_path)
df = df.iloc[:, :-1]

# Rename columns to match Prisma model
df.columns = ["datetime", "open", "high", "low", "close", "volume"]

# Convert datetime column to actual datetime format
df["datetime"] = pd.to_datetime(df["datetime"])

# Round decimal values to 3 decimal places
df[["open", "high", "low", "close"]] = df[["open", "high", "low", "close"]].round(3)

# Prisma database insertion
async def insert_data():
    db = Prisma()
    await db.connect()

    try:
        # Delete existing data to prevent unique constraint error
        await db.stockdata.delete_many()

        # Insert new data
        records = df.to_dict(orient="records")
        await db.stockdata.create_many(data=records)
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        await db.disconnect()

# Run the async function
asyncio.run(insert_data())
