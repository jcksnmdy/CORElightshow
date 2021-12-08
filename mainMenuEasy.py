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

os.system("pip3 install twilio")
from twilio.rest import Client

clientIdHalf = 'ACa34bd8ffed125040'
ClientIdOther = '6642b1801b24da28'
halfAuth = "8f31f5a2178908"
otherAuth = "926794f25fb427bff9"
# the following line needs your Twilio Account SID and Auth Token
messenger = Client(clientIdHalf+ClientIdOther, halfAuth+otherAuth)

morningMusic = 7
nightMusic = 18
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


    if (int(current_time[0:2])>close) and (int(current_time[3:5])<15) and (int(current_time[0:2])<close+1):
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Shutting Down Flags")
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "shutdown")
        playMusic.shutdownMessage()
        print("CLOSE")
        time.sleep(21600)

    elif (int(current_time[0:2])>nightMusic) and (int(current_time[0:2])<close):
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Starting Galactic Golf")
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
        time.sleep(30)
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "start")
        askReady()
        welcomeMessage()
        hour = (close-int(current_time[0:2]))-1
        minute = (int(current_time[3:5]))
        messenger.messages.create(to="+18658046479", 
                    from_="+12185271160", 
                    body="Playing Songs " + hour + ":" + 53-minute + " Left")
        running = True
        rand = random.sample(range(numSongs), numSongs)
        count = 0
        print(str(rand))
        while running:
            if (hour <= 0) and (minute > 40):
                playMusic.play(station, 53-minute, "pew")
                playMusic.playSong(rand, count)
                os.system("mosquitto_pub -h localhost -t test_channel -m " + "shutdown")
                playMusic.shutdownMessage()
                print("CLOSE")
                time.sleep(1800)
                os.system("sudo reboot")
            else:
                print("playing pandora for 13 minutes")
                playMusic.playPandora(station, 13, "pew")
                print("Playing rogrammed song")
                playMusic.playSong(rand, count)
                count+=1
                pygame.mixer.music.stop()
                time.sleep(10)
                    #loop = hourss-minutess
            #print("Loop playing songs num: " + str(loop) + "minutes" + current_time[3:5] + " " + str(hourss) + " " + str(minutess))

        
    elif (int(current_time[0:2])>morningMusic) and (int(current_time[0:2])<nightMusic):
        minutes = (((nightMusic-int(current_time[0:2]))*60)-60)+(60-int(current_time[3:5]))
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Playing morning Music for " + minutes + " minutes")
        print("Minutes playing regular: " + str(minutes+5))
        playMusic.playPandora(station, minutes, "pew")

    time.sleep(1)
        
        