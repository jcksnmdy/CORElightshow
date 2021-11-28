import pandas as pd
import pygame
import os
import time
import random
import subprocess
import signal
import threading
import playMusic
import sys
from funAudio import welcomeMessage
import paho.mqtt.client as mqtt
from games import startTargetGame, startKnockOutGame, startCaptureGame, askReady, startPopupGame
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht, path
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    while current_time != "07:00:00":
        time.sleep(0.5)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)

    current_time = "00:00:00"
    print("Starting music for: ")
    station = fridayHits
    loop = 10
    if (datetime.today().isoweekday() == 1):
        print("Monday")
        station = monHipHop
        playMusic.playPandora(station, 840, "pew")
    else:
        if (datetime.today().isoweekday() == 2):
            print("Tuesday")
            station = tuesRock
            loop = 12
        if (datetime.today().isoweekday() == 3):
            print("Wednesday")
            station = wedWayBack
            loop = 12
        if (datetime.today().isoweekday() == 4):
            print("Thursday")
            station = thursThrowback
            loop = 12
        if (datetime.today().isoweekday() == 5):
            print("Friday")
            station = fridayHits
            loop = 16
        if (datetime.today().isoweekday() == 6):
            print("Saturday")
            station = satDisco
            loop = 16
        if (datetime.today().isoweekday() == 7):
            print("Sunday")
            station = sunCountry
            loop = 8

        playMusic.playPandora(station, 660, "pew")
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
        time.sleep(30)
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "start")
        askReady()
        welcomeMessage()
        playMusic.play(station, 15, "pew", loop)
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "shutdown")
        playMusic.shutdownMessage()
        print("CLOSE")
        