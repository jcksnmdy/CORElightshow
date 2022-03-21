import pandas as pd
import pygame
import os
import time
import random
import subprocess
import signal
import threading
import datetime
import pygame_widgets
import paho.mqtt.client as mqtt
import broadcastDisplay
from broadcastDisplay import showTargets, stopbutton, showStop, pulseRed, pulseOrange, pulseWhite, pulseYellow, pulseGreen, pulseBlue, sparkleRed, whiteFlagOuter, redFlagOuter, orangeFlagOuter, blueFlagOuter, greenFlagOuter, yellowFlagOuter, setHit, getHit, refresh, setRedFlagSame, setOrangeFlagSame, setWhiteFlagSame, setGreenFlagSame, setBlueFlagSame, setYellowFlagSame
import sys
sys.path.append('/home/pi/Desktop/globals/')
#sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numStations, holiday, michealJ, yacht, path

MQTT_SERVER = "192.168.99.93"
#MQTT_SERVER = "192.168.1.228"

MQTT_PATH = "test_channel"
globalSoundEffect = "pew"
numSongs = 20
grey = (128,128,128)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if("hit" in str(msg.payload) and "red" not in str(msg.payload) and "yellow" not in str(msg.payload) and "orange" not in str(msg.payload) and "green" not in str(msg.payload) and "blue" not in str(msg.payload) and "white" not in str(msg.payload)):
        print("hittt")
        pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/effects/" + globalSoundEffect + ".mp3")
        pygame.mixer.music.play(0)

 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
#client.connect(MQTT_SERVER, 1883, 60)

def toTuple(before):
    firstNum = float(before[before.find("(")+1:before.find(",")])
    secNum = float(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = float(before[before.find(",", 9)+2:before.find(")")])
    returning = (firstNum, secNum, thirdNum)
    return returning

pygame.init()
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Programmer")
def playSong(rand, count):
    global now, current_time
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    time.sleep(3)
    os.system("mosquitto_pub -h localhost -t test_channel -m " + 'load' + str(rand[count]+1))
    time.sleep(10)
    os.system("mosquitto_pub -h localhost -t test_channel -m " + 'song' + str(rand[count]+1))
    pygame.mixer.music.load(path + "/songs/song" + str(rand[count]+1) + ".mp3")
    
    
    print("Programmed song playing. Programmed song count: " + str(count+1) + ". Song index: " + str(rand[count]+1) + "")
    i = 0
    pygame.mixer.music.play(0)
    #os.system("sudo /home/pi/PI_FM/fm_transmitter/fm_transmitter -f 96.7 -r /home/pi/Desktop/songs/song" + str(rand[count]+1) + ".wav")
    allInfo = pd.read_excel(path + "/flagCode/song" + str(rand[count]+1) + ".xlsx")
    
    while (pygame.mixer.music.get_busy()):
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                #checkEventMain(mouse_pos)
        if (i+2 < len(allInfo)):
            broadcastDisplay.troubleShootTextBroadcast("", "Playing song: " + str(count+1))
            broadcastDisplay.setRedFlag(toTuple(allInfo.loc[(i),'red Left']), toTuple(allInfo.loc[(i),'red Middle']), toTuple(allInfo.loc[(i),'red Right']), redFlagOuter)
            broadcastDisplay.setOrangeFlag(toTuple(allInfo.loc[(i),'orange Left']), toTuple(allInfo.loc[(i),'orange Middle']), toTuple(allInfo.loc[(i),'orange Right']), orangeFlagOuter)
            broadcastDisplay.setWhiteFlag(toTuple(allInfo.loc[(i),'white Left']), toTuple(allInfo.loc[(i),'white Middle']), toTuple(allInfo.loc[(i),'white Right']), whiteFlagOuter)
            broadcastDisplay.setGreenFlag(toTuple(allInfo.loc[(i),'green Left']), toTuple(allInfo.loc[(i),'green Middle']), toTuple(allInfo.loc[(i),'green Right']), greenFlagOuter)
            broadcastDisplay.setYellowFlag(toTuple(allInfo.loc[(i),'yellow Left']), toTuple(allInfo.loc[(i),'yellow Middle']), toTuple(allInfo.loc[(i),'yellow Right']), yellowFlagOuter)
            broadcastDisplay.setBlueFlag(toTuple(allInfo.loc[(i),'blue Left']), toTuple(allInfo.loc[(i),'blue Middle']), toTuple(allInfo.loc[(i),'blue Right']), blueFlagOuter)
        else:
            broadcastDisplay.setRedFlag(grey, grey, grey, redFlagOuter)
            broadcastDisplay.setOrangeFlag(grey, grey, grey, orangeFlagOuter)
            broadcastDisplay.setWhiteFlag(grey, grey, grey, whiteFlagOuter)
            broadcastDisplay.setGreenFlag(grey, grey, grey, greenFlagOuter)
            broadcastDisplay.setYellowFlag(grey, grey, grey, yellowFlagOuter)
            broadcastDisplay.setBlueFlag(grey, grey, grey, blueFlagOuter)
        i+=1
        time.sleep(0.06)


        pygame.display.flip()
        
        clock.tick(60)
    pygame.mixer.music.stop()

def shutdownMessage():
    global now, current_time
    pygame.mixer.music.load(path + "/songs/closingTime.mp3")
    print("shutting down")
    i = 0
    pygame.mixer.music.play(0)

    #os.system("sudo /home/pi/PI_FM/fm_transmitter/fm_transmitter -f 96.7 -r /home/pi/Desktop/songs/song" + str(rand[count]+1) + ".wav")
    #allInfo = pd.read_excel(path + "/flagCode/song" + str(rand[count]+1) + ".xlsx")
    while (pygame.mixer.music.get_busy()):
        broadcastDisplay.troubleShootTextBroadcast("Shutting down", "Playing Shutdown song")
        time.sleep(0.01)

def playPandora(playlist, delay, soundEffect):
    global globalSoundEffect, count
    globalSoundEffect = soundEffect
    print(globalSoundEffect)
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + str("red") + str(1))
    os.system("mosquitto_pub -h localhost -t test_channel -m " + str("orange") + str(2))
    os.system("mosquitto_pub -h localhost -t test_channel -m " + str("yellow") + str(3))
    os.system("mosquitto_pub -h localhost -t test_channel -m " + str("blue") + str(4))
    os.system("mosquitto_pub -h localhost -t test_channel -m " + str("green") + str(5))
    os.system("mosquitto_pub -h localhost -t test_channel -m " + str("white") + str(6))
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "wait")
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    print(proc.pid)
    timer = 0
    
    client.loop_start()
    while timer < delay*60:
        time.sleep(0.01)
        timer+=0.01
        showStop()
        refresh()
        broadcastDisplay.troubleShootTextBroadcast("", "Pandora: " + str(playlist) + ", " + str(((delay*60)-timer)/60) + " minutes")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if redFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitred")


                if whiteFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitwhite")


                if orangeFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitorange")


                if yellowFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hityellow")


                if greenFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitgreen")


                if blueFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitblue")

                if stopbutton.collidepoint(mouse_pos):
                    stop(proc.pid)
                    print("Done")
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    client.loop_stop()
                    timer = 9999999999999999999999
                    count = 99999999999
                    break
    print("Done with pandora")
    stop(proc.pid)

def play(playlist, delay, soundEffect):
    global count
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    #client.loop_forever()
    count = 0
    rand = random.sample(range(numSongs), numSongs)
    print(str(rand) + " Delay: " + str(delay))
    while count < numSongs:
        playSong(rand, count)
        count+=1
        pygame.mixer.music.stop()
        #os.system("mosquitto_pub -h localhost -t test_channel -m " + str(4))
        #pandoraA = threading.Thread(group=None, target=playPandora, args=("playlist, delay,"), name=None)
        #pandoraA.start()
        time.sleep(15)
        playPandora(playlist, delay, globalSoundEffect)
    print("Yep Done")

def play(playlist, delay, soundEffect, loopLength):
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    #client.loop_forever()
    count = 0
    rand = random.sample(range(numSongs), numSongs)
    print(str(rand) + " Delay: " + str(delay))
    while count < loopLength:
        playSong(rand, count)
        count+=1
        pygame.mixer.music.stop()
        #os.system("mosquitto_pub -h localhost -t test_channel -m " + str(4))
        #pandoraA = threading.Thread(group=None, target=playPandora, args=("playlist, delay,"), name=None)
        #pandoraA.start()
        time.sleep(10)
        playPandora(playlist, delay, globalSoundEffect)
    print("Yep Done")
    
def stop(id):
    pygame.mixer.music.stop()
    pygame.mixer.music.stop()
    os.killpg(id, signal.SIGTERM)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()