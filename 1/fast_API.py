from fastapi import FastAPI
import json
import os

app = FastAPI()

FILE_PATH = "payloads.json"

def read():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return [] 
    return []

def write(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)

@app.post("/append")
async def append_payload(payload: dict):
    data = read()
    data.append(payload)
    write(data)
    return {"message": "Payload appended successfully"}

@app.get("/last_payloads")
async def get_last_payloads():
    data = read()
    return data[-10:]