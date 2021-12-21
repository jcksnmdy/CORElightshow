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
from games import askReady
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht, path
from datetime import datetime

from twilio.rest import Client

clientIdHalf = 'ACa34bd8ffed125040'
ClientIdOther = '6642b1801b24da28'
halfAuth = "8f31f5a2178908"
otherAuth = "926794f25fb427bff9"
# the following line needs your Twilio Account SID and Auth Token
messenger = Client(clientIdHalf+ClientIdOther, halfAuth+otherAuth)
        
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Main Menu Easy Started" + str(now))

MSTARTTIME = 7
GOLFTIME = 17
CLOSETIME = 21

morningMusic = now.replace(hour=MSTARTTIME, minute=0, second=0, microsecond=0)
nightMusic = now.replace(hour=GOLFTIME, minute=30, second=0, microsecond=0)
nightMusicEnd = now.replace(hour=CLOSETIME-1, minute=45, second=0, microsecond=0)
close = now.replace(hour=CLOSETIME, minute=0, second=0, microsecond=0)
gone = now.replace(hour=CLOSETIME, minute=15, second=0, microsecond=0)

print("Open: " + str(morningMusic) + " Start: " + str(nightMusic) + " End: " + str(nightMusicEnd) + " Close: " + str(close) + " Leaving: " + str(gone))
messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Open: " + str(morningMusic) + " Start: " + str(nightMusic) + " End: " + str(nightMusicEnd) + " Close: " + str(close) + " Leaving: " + str(gone))
test = now.replace(hour=3, minute=20, second=0, microsecond=0)
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
midday = now.replace(hour=12, minute=0, second=0, microsecond=0)



while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

    print("Starting music for: ")
    if (datetime.today().isoweekday() == 1):
        print("Monday")
        station = monHipHop
    if (datetime.today().isoweekday() == 2):
        print("Tuesday")
        station = tuesRock
        loop = 12
        CLOSETIME = 21
    if (datetime.today().isoweekday() == 3):
        print("Wednesday")
        station = wedWayBack
        loop = 12
        CLOSETIME = 21
    if (datetime.today().isoweekday() == 4):
        print("Thursday")
        station = thursThrowback
        loop = 12
        CLOSETIME = 21
    if (datetime.today().isoweekday() == 5):
        print("Friday")
        station = fridayHits
        loop = 16
        CLOSETIME = 22
    if (datetime.today().isoweekday() == 6):
        print("Saturday")
        station = satDisco
        loop = 16
        CLOSETIME = 22
    if (datetime.today().isoweekday() == 7):
        print("Sunday")
        station = sunCountry
        loop = 8
        CLOSETIME = 20
    nightMusicEnd = now.replace(hour=CLOSETIME-1, minute=45, second=0, microsecond=0)
    close = now.replace(hour=CLOSETIME, minute=0, second=0, microsecond=0)
    gone = now.replace(hour=CLOSETIME, minute=15, second=0, microsecond=0)

    if (now>=close) and (now<=gone):
        print("Shutting down")
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Shutting Down Flags")
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "shutdown")
        playMusic.shutdownMessage()
        print("CLOSE")
        time.sleep(54000)

    elif (now>=nightMusic) and (now<=nightMusicEnd) and (now!=midnight) and (now!=midday):
        print("Starting Galactic Golf")
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Starting Galactic Golf")
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
        time.sleep(20)
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "start")
        print("Asking Ready")
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Asking Ready")
        askReady()
        print("Playing Opening")
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Playing Opening")
        welcomeMessage()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        hour = (close-int(current_time[0:2]))-1
        minute = (int(current_time[3:5]))
        print("Playing music now")
        messenger.messages.create(to="+18658046479", 
                    from_="+12185271160", 
                    body="Playing Songs " + hour + ":" + 53-minute + " Left")
        running = True
        rand = random.sample(range(numSongs), numSongs)
        count = 0
        print(str(rand))
        while running:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if (now<=nightMusicEnd):
                print("playing pandora for 11 minutes")
                playMusic.playPandora(station, 11, "pew")
                print("Playing rogrammed song")
                playMusic.playSong(rand, count)
                count+=1
                pygame.mixer.music.stop()
                time.sleep(5)
            else:
                print("Preparing shutdown from galactic golf")
                messenger.messages.create(to="+18658046479", 
                    from_="+12185271160", 
                    body="Preparing shutdown from galactic golf")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                minShutdown = int(current_time[3:5])
                if (minShutdown<53):
                    playMusic.play(station, 53-minShutdown, "pew")
                playMusic.playSong(rand, count)
                os.system("mosquitto_pub -h localhost -t test_channel -m " + "shutdown")
                playMusic.shutdownMessage()
                print("CLOSE")
                time.sleep(1800)
                running = False
            os.system("sudo reboot")                
                    #loop = hourss-minutess
            #print("Loop playing songs num: " + str(loop) + "minutes" + current_time[3:5] + " " + str(hourss) + " " + str(minutess))

        
    elif (now>=morningMusic) and (now<=nightMusic):
        minutes = ((((GOLFTIME-int(current_time[0:2]))*60)-60)+(62-int(current_time[3:5])))+15
        messenger.messages.create(to="+18658046479", 
                       from_="+12185271160", 
                       body="Playing morning Music for " + str(minutes) + " minutes")
        print("Minutes playing regular: " + str(minutes))
        playMusic.playPandora(station, minutes, "pew")

    time.sleep(10)
