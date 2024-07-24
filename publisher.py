import paho.mqtt.client as paho
import random
import time
import json
import sys

def read_temperature():
    # Simulate reading temperature from a sensor
    return round(random.uniform(16.0, 25.0), 2)

def main():
    client = paho.Client()

    if client.connect("localhost", 1883, 60) != 0:
        print("Connection failed")
        sys.exit(-1)

    try:
        while True:
            temperature = read_temperature()
            payload = json.dumps({"temperature": round(temperature,2), "timestamp": int(time.time())})            
            client.publish("hotel/temperature", payload, qos=0)
            time.sleep(60)
    except:
        print("Publisher stopped")

    client.disconnect()

if __name__ == "__main__":
    main()
~                   
