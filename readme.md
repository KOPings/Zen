Follwoing things needs to be installed

FastAPI (for HTTPS)

uvicorn (Server)

paho-mqtt (MQTT) 

mosquitto ( For MQTT broker)


To run this program
First start the mosquitto service on default port (1883)

run the follwing command in new terminal(mosquitto_sub -t hotel/temperature) 

run the publisher.py in the new terminal

run the subscriber.py in the new terminal

run the api_web.py in the new terminal

To access the webpage use the following URL : http://127.0.0.1:8000/latest-temperature