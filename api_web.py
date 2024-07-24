from fastapi import FastAPI
from typing import Dict, Union
import json
import os

app = FastAPI()

def read_latest_data() -> Union[Dict[str, Union[str, float, int]], Dict[str, str]]:
    if os.path.exists("temperature_data.json"):
        with open("temperature_data.json", "r") as f:
            data_points = json.load(f)
            if data_points:
                latest_data = data_points[-1]
                return {"temperature": latest_data[0], "timestamp": latest_data[1]}
    return {"error": "No data available"}

@app.get("/")
def get_latest_temperature():
    return read_latest_data()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
