from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
import random
import time

import ssl
import scanf
import serial

import numpy as np
from time import sleep

import paho.mqtt.client as mqtt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.label = QLabel()
        self.layout.addWidget(self.label, 0, 0)

        self.line = QLineEdit()
        self.layout.addWidget(self.line, 0, 1)
        self.line.setText("text")

        self.button = QPushButton()
        self.layout.addWidget(self.button, 0, 2)
        self.button.setText("PUBLISH")

        def setnTicks():
            value = int(self.line.text())
            client.publish('base/state/nTicks', value)

        self.button.clicked.connect(setnTicks)


class LogicThread(QtCore.QThread):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        window = self.window
        while True:
            client.publish('base/state/humidity', float(np.random.randint(0, 100, 1)))
            client.publish('base/state/temperature', float(np.random.randint(0, 100, 1)))
            sleep(1)


# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe('$SYS/#')


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    window.label.setText(str(msg.payload))


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

application = QApplication(sys.argv)
window = MainWindow()
window.show()

thread = LogicThread(window)
thread.start()

sys.exit(application.exec())