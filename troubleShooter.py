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
from broadcastDisplay import pulseRed, pulseOrange, pulseWhite, pulseYellow, pulseGreen, pulseBlue, sparkleRed, whiteFlagOuter, redFlagOuter, orangeFlagOuter, blueFlagOuter, greenFlagOuter, yellowFlagOuter, setHit, getHit, refresh, showStop, stopbutton, redFlagLeftOrig, orangeFlagLeftOrig, whiteFlagLeftOrig, yellowFlagLeftOrig, greenFlagLeftOrig, blueFlagLeftOrig, setRedFlagSame, setOrangeFlagSame, setWhiteFlagSame, setGreenFlagSame, setBlueFlagSame, setYellowFlagSame
from playMusic import stop

from games import startTargetGame, startKnockOutGame, startCaptureGame, askReady
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht

red = (255,0,0)
orange = (255,128,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)
white = (255,255,255)
darkred = (255/2,0,0)
darkorange = (255/2,128/2,0)
darkblue = (0,0,255/2)
darkyellow = (255/2,255/2,0)
darkgreen = (0,255/2,0)
grey = (128,128,128)
black = (0,0,0)

redLives = 3
orangeLives = 3
whiteLives = 3
yellowLives = 3
greenLives = 3
blueLives = 3
popUp = False

pulseR = threading.Thread(group=None, target=pulseBlue, name=None)
pulseO = threading.Thread(group=None, target=pulseBlue, name=None)
pulseW = threading.Thread(group=None, target=pulseBlue, name=None)
pulseY = threading.Thread(group=None, target=pulseBlue, name=None)
pulseG = threading.Thread(group=None, target=pulseBlue, name=None)
pulseB = threading.Thread(group=None, target=pulseBlue, name=None)

globalSound = "pew"
MQTT_SERVER = "192.168.99.93"
MQTT_PATH = "test_channel"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
reds = 3
blues = 3
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global pulseR, pulseO, pulseW, pulseY, pulseG, pulseB, reds, blues, red, blue, black, grey, redReady, orangeReady, whiteReady, greenReady, yellowReady, blueReady, popUp, redLives, orangeLives, whiteLives, yellowLives, greenLives, blueLives
    print(msg.topic+" "+str(msg.payload))
    
    if ("redStatus:rK" in str(msg.payload)):
        reds+=1
        blues-=1
        setRedFlagSame(red, redFlagLeftOrig)
    if ("orangeStatus:rK" in str(msg.payload)):
        reds+=1
        blues-=1
        setOrangeFlagSame(red, orangeFlagLeftOrig)
    if ("yellowStatus:rK" in str(msg.payload)):
        reds+=1
        blues-=1
        setYellowFlagSame(red, yellowFlagLeftOrig)
    if ("greenStatus:rK" in str(msg.payload)):
        reds+=1
        blues-=1
        setGreenFlagSame(red, greenFlagLeftOrig)
    if ("blueStatus:rK" in str(msg.payload)):
        reds+=1
        blues-=1
        setBlueFlagSame(red, blueFlagLeftOrig)
    if ("whiteStatus:rK" in str(msg.payload)):
        reds+=1
        blues-=1
        setWhiteFlagSame(red, whiteFlagLeftOrig)
    if ("redStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setRedFlagSame(blue, redFlagLeftOrig)
    if ("orangeStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setOrangeFlagSame(blue, orangeFlagLeftOrig)
    if ("yellowStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setYellowFlagSame(blue, yellowFlagLeftOrig)
    if ("greenStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setGreenFlagSame(blue, greenFlagLeftOrig)
    if ("blueStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setBlueFlagSame(blue, blueFlagLeftOrig)
    if ("whiteStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setWhiteFlagSame(blue, whiteFlagLeftOrig)
    if ("got:red" in str(msg.payload)):
        pygame.mixer.music.load("effects/redCaptured.mp3")
        setRedFlagSame(grey, redFlagLeftOrig)
        pygame.mixer.music.play(0)
    if ("got:blue" in str(msg.payload)):
        pygame.mixer.music.load("effects/blueCaptured.mp3")
        setBlueFlagSame(grey, blueFlagLeftOrig)
        pygame.mixer.music.play(0)
    if ("got:green" in str(msg.payload)):
        pygame.mixer.music.load("effects/greenCaptured.mp3")
        setGreenFlagSame(grey, greenFlagLeftOrig)
        pygame.mixer.music.play(0)
    if ("got:white" in str(msg.payload)):
        pygame.mixer.music.load("effects/whiteCaptured.mp3")
        setWhiteFlagSame(grey, whiteFlagLeftOrig)
        pygame.mixer.music.play(0)
    if ("got:yellow" in str(msg.payload)):
        pygame.mixer.music.load("effects/yellowCaptured.mp3")
        setYellowFlagSame(grey, yellowFlagLeftOrig)
        pygame.mixer.music.play(0)
    if ("got:orange" in str(msg.payload)):
        pygame.mixer.music.load("effects/orangeCaptured.mp3")
        setOrangeFlagSame(grey, orangeFlagLeftOrig)
        pygame.mixer.music.play(0)

    if ("hit" in str(msg.payload) and "red" not in str(msg.payload) and "orange" not in str(msg.payload) and "white" not in str(msg.payload) and "yellow" not in str(msg.payload) and "green" not in str(msg.payload) and "blue" not in str(msg.payload)):
        setHit(True)
        if(pulseR.is_alive()):
            pulseR.join()
        if(pulseO.is_alive()):
            pulseO.join()
        if(pulseW.is_alive()):
            pulseW.join()
        if(pulseY.is_alive()):
            pulseY.join()
        if(pulseG.is_alive()):
            pulseG.join()
        if(pulseB.is_alive()):
            pulseB.join()

    if ("stop" in str(msg.payload)):
        if(pulseR.is_alive()):
            pulseR.join()
        if(pulseO.is_alive()):
            pulseO.join()
        if(pulseW.is_alive()):
            pulseW.join()
        if(pulseY.is_alive()):
            pulseY.join()
        if(pulseG.is_alive()):
            pulseG.join()
        if(pulseB.is_alive()):
            pulseB.join()

        redLives = 3
        orangeLives = 3
        whiteLives = 3
        yellowLives = 3
        greenLives = 3
        blueLives = 3
        popUp = False
        setRedFlagSame(grey, redFlagLeftOrig)
        setBlueFlagSame(grey, blueFlagLeftOrig)
        setGreenFlagSame(grey, greenFlagLeftOrig)
        setWhiteFlagSame(grey, whiteFlagLeftOrig)
        setYellowFlagSame(grey, yellowFlagLeftOrig)
        setOrangeFlagSame(grey, orangeFlagLeftOrig)


    if ("targetGameR" in str(msg.payload)):
        print("RED")
        if(pulseR.is_alive()):
            pulseR.join()
        pulseR = threading.Thread(group=None, target=pulseRed, name=None)
        pulseR.start()
    if ("targetGameO" in str(msg.payload)):
        print("ORANGE")
        if(pulseO.is_alive()):
            pulseO.join()
        pulseO = threading.Thread(group=None, target=pulseOrange, name=None)
        pulseO.start()
    if ("targetGameW" in str(msg.payload)):
        print("WHITE")
        if(pulseW.is_alive()):
            pulseW.join()
        pulseW = threading.Thread(group=None, target=pulseWhite, name=None)
        pulseW.start()
    if ("targetGameY" in str(msg.payload)):
        print("YELLOW")
        if(pulseY.is_alive()):
            pulseY.join()
        pulseY = threading.Thread(group=None, target=pulseYellow, name=None)
        pulseY.start()
    if ("targetGameG" in str(msg.payload)):
        print("GREEN")
        if(pulseG.is_alive()):
            pulseG.join()
        pulseG = threading.Thread(group=None, target=pulseGreen, name=None)
        pulseG.start()
    if ("targetGameB" in str(msg.payload)):
        print("BLUE")
        if(pulseB.is_alive()):
            pulseB.join()
        pulseB = threading.Thread(group=None, target=pulseBlue, name=None)
        pulseB.start()
    

    if ("capture" in str(msg.payload)):
        popUp = True

    if(popUp):
        if ("red" in str(msg.payload)):
            redLives-=1
        if ("orange" in str(msg.payload)):
            orangeLives-=1
        if ("white" in str(msg.payload)):
            whiteLives-=1
        if ("yellow" in str(msg.payload)):
            yellowLives-=1
        if ("green" in str(msg.payload)):
            greenLives-=1
        if ("blue" in str(msg.payload)):
            blueLives-=1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 19)
screen = pygame.display.set_mode((750, 550))
clock = pygame.time.Clock()
pygame.display.set_caption("Trouble Shooter")


restartRed = pygame.Rect(10, 10, 150, 25)
restartRedText = font.render('Restart Red', True, black)
restartOrange = pygame.Rect(10, 40, 150, 25)
restartOrangeText = font.render('Restart Orange', True, black)
restartWhite = pygame.Rect(10, 70, 150, 25)
restartWhiteText = font.render('Restart White', True, black)
restartGreen = pygame.Rect(10, 100, 150, 25)
restartGreenText = font.render('Restart Green', True, black)
restartYellow = pygame.Rect(10, 130, 150, 25)
restartYellowText = font.render('Restart Yellow', True, black)
restartBlue = pygame.Rect(10, 160, 150, 25)
restartBlueText = font.render('Restart Blue', True, black)
restartAll = pygame.Rect(10, 190, 150, 25)
restartAllText = font.render('Restart All', True, black)

stop = pygame.Rect(10, 220, 150, 25)
stopText = font.render('STOP', True, black)


# Load the main Menu
def main():

    global redLives, orangeLives, whiteLives, yellowLives, greenLives, blueLives

    while True:
        
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                
                if restartRed.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:red")
                if restartOrange.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:orange")
                if restartWhite.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:white")
                if restartGreen.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:green")
                if restartYellow.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:yellow")
                if restartBlue.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:blue")
                if stop.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "endstop")

                if restartAll.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:red")
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:orange")
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:white")
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:green")
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:yellow")
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "restart:blue")
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "endstop")

        redLifeText = font.render(str(redLives), True, black)
        orangeLifeText = font.render(str(orangeLives), True, black)
        whiteLifeText = font.render(str(whiteLives), True, black)
        yellowLifeText = font.render(str(yellowLives), True, black)
        greenLifeText = font.render(str(greenLives), True, black)
        blueLifeText = font.render(str(blueLives), True, black)
        
        pygame.draw.rect(screen, white, restartAll)  # draw button
        screen.blit(restartAllText, restartAll)
        pygame.draw.rect(screen, white, restartRed)  # draw button
        screen.blit(restartRedText, restartRed)
        pygame.draw.rect(screen, white, restartOrange)  # draw button
        screen.blit(restartOrangeText, restartOrange)
        pygame.draw.rect(screen, white, restartWhite)  # draw button
        screen.blit(restartWhiteText, restartWhite)
        pygame.draw.rect(screen, white, restartGreen)  # draw button
        screen.blit(restartGreenText, restartGreen)
        pygame.draw.rect(screen, white, restartYellow)  # draw button
        screen.blit(restartYellowText, restartYellow)
        pygame.draw.rect(screen, white, restartBlue)  # draw button
        screen.blit(restartBlueText, restartBlue)
        pygame.draw.rect(screen, white, stop)  # draw button
        screen.blit(stopText, stop)

        refresh()

        screen.blit(redLifeText, (120, 330))
        screen.blit(orangeLifeText, (450, 280))
        screen.blit(whiteLifeText, (340, 190))
        screen.blit(yellowLifeText, (150, 220))
        screen.blit(greenLifeText, (240, 160))
        screen.blit(blueLifeText, (470, 100))

        pygame.display.flip()
        
        clock.tick(60)


main()