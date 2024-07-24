
import paho.mqtt.client as paho
import json
import time
import sys
from datetime import datetime

TEMPERATURE_THRESHOLD = 22.0
DURATION_THRESHOLD = 5*60  # 5 minutes in seconds
data_points = []

def on_message(client, userdata, msg):
    global data_points, alarm_triggered
    payload = json.loads(msg.payload.decode())
    temperature = payload["temperature"]
    timestamp = payload["timestamp"]
    f_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    data_points.append((temperature, f_timestamp))

        # Save data points locally
    with open("temperature_data.json", "w") as f:
        json.dump(data_points, f)
    if len(data_points) > 5:
        data_points.pop(0)

    if len(data_points) == 5 and all(point[0] > TEMPERATURE_THRESHOLD for point in data_points):
        print("ALARM: Temperature has been above threshold for the last 5 data points!")

def main():
    client = paho.Client()
    client.on_message = on_message

    if client.connect("localhost", 1883, 60) != 0:
        print("Connection failed")
        sys.exit(-1)

    client.subscribe("hotel/temperature")

    try:
        print("Press Ctrl+C to exit ...")
        client.loop_forever()
    except KeyboardInterrupt:
        print("Subscriber stopped")

    client.disconnect()

if __name__ == "__main__":
    main()
