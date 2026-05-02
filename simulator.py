import requests
import time
import random

URL = "http://127.0.0.1:8000/data"

while True:
    data = {
        "device_id": 2,
        "temperature": random.uniform(20, 60)
    }

    try:
        response = requests.post(URL, json=data)
        print("Status:", response.status_code)
        print("Sent:", data)
    except Exception as e:
        print("Error:", e)

    time.sleep(2)