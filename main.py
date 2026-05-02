from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔥 THIS FIXES YOUR DASHBOARD (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

devices = []
data_store = []

class Device(BaseModel):
    name: str

class SensorData(BaseModel):
    device_id: int
    temperature: float

@app.get("/")
def home():
    return {"message": "IoT API Running"}

@app.post("/add_device")
def add_device(device: Device):
    device_id = len(devices) + 1
    devices.append({"id": device_id, "name": device.name})
    return {"device_id": device_id}

@app.post("/data")
def add_data(data: SensorData):
    data_store.append({
        "device_id": data.device_id,
        "temperature": data.temperature
    })
    return {"status": "data added"}

@app.get("/data")
def get_data():
    return data_store