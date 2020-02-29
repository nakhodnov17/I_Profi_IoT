import ssl
import scanf
import serial

import numpy as np
from time import sleep

import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe('$SYS/#')


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))


use_logger, use_auth = True, True

client_id = 'mqtt-iprofi_101914952-6y49xq'
username, password = 'maksim64', 'simplepassword'
host, port, keepalive = 'sandbox.rightech.io', 1883, 60

client = mqtt.Client(client_id=client_id)
client.on_connect = on_connect
client.on_message = on_message

if use_logger:
    client.enable_logger(logger=None)
if use_auth:
    client.username_pw_set(username=username, password=password)

client.connect(host=host, port=port, keepalive=keepalive)

client.loop_start()

with serial.Serial('COM3', 9600) as reader:
    while True:
        line = reader.readline().decode().strip()
        humidity, temperature = scanf.scanf("Humidity: %f\tTemperature: %f", line)

        client.publish('base/state/humidity', humidity)
        client.publish('base/state/temperature', temperature)

client.disconnect()
