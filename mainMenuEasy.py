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

morningMusic = 7
nightMusic = 17
close = 21

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time[0:2])

    print("Starting music for: ")
    if (datetime.today().isoweekday() == 1):
        print("Monday")
        station = monHipHop
    if (datetime.today().isoweekday() == 2):
        print("Tuesday")
        station = tuesRock
        loop = 12
        close = 21
    if (datetime.today().isoweekday() == 3):
        print("Wednesday")
        station = wedWayBack
        loop = 12
        close = 21
    if (datetime.today().isoweekday() == 4):
        print("Thursday")
        station = thursThrowback
        loop = 12
        close = 21
    if (datetime.today().isoweekday() == 5):
        print("Friday")
        station = fridayHits
        loop = 16
        close = 22
    if (datetime.today().isoweekday() == 6):
        print("Saturday")
        station = satDisco
        loop = 16
        close = 22
    if (datetime.today().isoweekday() == 7):
        print("Sunday")
        station = sunCountry
        loop = 8
        close = 20


    if (int(current_time[0:2])>close):
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "shutdown")
        playMusic.shutdownMessage()
        print("CLOSE")

    elif (int(current_time[0:2])>nightMusic):
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
        time.sleep(30)
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "start")
        askReady()
        #welcomeMessage()
        hourss = (close-int(current_time[0:2])*4)
        minutess = ((int(current_time[3:5]))/13)
        loop = (close-int(current_time[0:2])*4)-
        print("Loop playing songs num: " + str(loop) + "minutes" + current_time[3:5] + " " + str(hourss) + " " + str(minutess))
        playMusic.play(station, 13, "pew", loop)
        
    elif (int(current_time[0:2])>morningMusic):
        minutes = ((nightMusic-int(current_time[0:2]*60))-60)+int(current_time[3:5])
        print("Minutes playing regular: " + str(minutes))
        playMusic.playPandora(station, minutes, "pew")
        
        