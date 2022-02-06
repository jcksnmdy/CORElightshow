import pygame
import os
import time
import random
import subprocess
import signal
import threading
import playMusic
import sys
import paho.mqtt.client as mqtt
import broadcastDisplay
from broadcastDisplay import pulseRed, pulseOrange, pulseWhite, pulseYellow, pulseGreen, pulseBlue, sparkleRed, whiteFlagOuter, redFlagOuter, orangeFlagOuter, blueFlagOuter, greenFlagOuter, yellowFlagOuter, setHit, getHit, refresh, showStop, stopbutton, redFlagLeftOrig, orangeFlagLeftOrig, whiteFlagLeftOrig, yellowFlagLeftOrig, greenFlagLeftOrig, blueFlagLeftOrig, setRedFlagSame, setOrangeFlagSame, setWhiteFlagSame, setGreenFlagSame, setBlueFlagSame, setYellowFlagSame
from playMusic import stop


pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 19)
screen = pygame.display.set_mode((750, 550))
clock = pygame.time.Clock()
pygame.display.set_caption("Game Runner")

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

redReady = False
orangeReady = False
whiteReady = False
greenReady = False
yellowReady = False
blueReady = False

globalSound = "pew"
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the cnection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
reds = 3
blues = 3
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global reds, blues, red, blue, black, grey, redReady, orangeReady, whiteReady, greenReady, yellowReady, blueReady
    print(msg.topic+" "+str(msg.payload))
    if("Ready" in str(msg.payload)):
        if("red:Ready" in str(msg.payload)):
            redReady = True
            time.sleep(0.5)
            broadcastDisplay.setRedFlag(red, red, red, redFlagOuter)
        if("white:Ready" in str(msg.payload)):
            whiteReady = True
            time.sleep(0.5)
            broadcastDisplay.setWhiteFlag(white, white, white, whiteFlagOuter)
        if("orange:Ready" in str(msg.payload)):
            orangeReady = True
            time.sleep(0.5)
            broadcastDisplay.setOrangeFlag(orange, orange, orange, orangeFlagOuter)
        if("green:Ready" in str(msg.payload)):
            greenReady = True
            time.sleep(0.5)
            broadcastDisplay.setGreenFlag(green, green, green, greenFlagOuter)
        if("yellow:Ready" in str(msg.payload)):
            yellowReady = True
            time.sleep(0.5)
            broadcastDisplay.setYellowFlag(yellow, yellow, yellow, yellowFlagOuter)
        if("blue:Ready" in str(msg.payload)):
            blueReady = True
            broadcastDisplay.setBlueFlag(blue, blue, blue, blueFlagOuter)
            time.sleep(0.5)
        print("Red: " + str(redReady) + ", " + "White: " + str(whiteReady) + ", " + "Orange: " + str(orangeReady) + ", " + "Green: " + str(greenReady) + ", " + "Yellow: " + str(yellowReady) + ", " + "Blue: " + str(blueReady))
    if("hit" in str(msg.payload) and "red" not in str(msg.payload) and "yellow" not in str(msg.payload) and "orange" not in str(msg.payload) and "green" not in str(msg.payload) and "blue" not in str(msg.payload) and "white" not in str(msg.payload)):
        print("hittt")
        setHit(True)
        pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/effects/" + globalSound + ".mp3")
        pygame.mixer.music.play(0)
        time.sleep(0.5)

    if ("bK" in str(msg.payload)):
        blues+=1
        reds-=1
        print("Reds: " + str(reds) + ", Blues: " + str(blues))

    if ("rK" in str(msg.payload)):
        reds+=1
        blues-=1
        print("Reds: " + str(reds) + ", Blues: " + str(blues))
    

 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()

def askReady():
    global redReady, orangeReady, whiteReady, greenReady, yellowReady, blueReady
    redReady = False
    orangeReady = False
    whiteReady = False
    greenReady = False
    yellowReady = False
    blueReady = False
    print("Before loop")
    client.loop_start()
    time.sleep(5)
    print("afeter")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "testSilent:red")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "testSilent:orange")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "testSilent:white")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "testSilent:green")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "testSilent:yellow")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "testSilent:blue")
    broadcastDisplay.setRedFlag(grey, grey, grey, redFlagOuter)
    broadcastDisplay.setOrangeFlag(grey, grey, grey, orangeFlagOuter)
    broadcastDisplay.setWhiteFlag(grey, grey, grey, whiteFlagOuter)
    broadcastDisplay.setGreenFlag(grey, grey, grey, greenFlagOuter)
    broadcastDisplay.setYellowFlag(grey, grey, grey, yellowFlagOuter)
    broadcastDisplay.setBlueFlag(grey, grey, grey, blueFlagOuter)
    time.sleep(20)
    counter = 0
    while counter < 12:
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
        if (not redReady):
            broadcastDisplay.setRedFlag(grey, grey, grey, redFlagOuter)
        if (not orangeReady):
            broadcastDisplay.setOrangeFlag(grey, grey, grey, orangeFlagOuter)
        if (not whiteReady):
            broadcastDisplay.setWhiteFlag(grey, grey, grey, whiteFlagOuter)
        if (not greenReady):
            broadcastDisplay.setGreenFlag(grey, grey, grey, greenFlagOuter)
        if (not yellowReady):
            broadcastDisplay.setYellowFlag(grey, grey, grey, yellowFlagOuter)
        if (not blueReady):
            broadcastDisplay.setBlueFlag(grey, grey, grey, blueFlagOuter)
        if (redReady and orangeReady and whiteReady and greenReady and yellowReady and blueReady):
            client.loop_stop()
            print("DONE. ALL CONNECTED")
            counter = 105
        else:
            print("Retrying...Not connected")
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "start")
            time.sleep(10)
            counter+=1
        

        pygame.display.flip()
        
        clock.tick(60)
    print("Done. Moving on")


def startTargetGame(playlist, soundEffect):
    font = pygame.font.Font('freesansbold.ttf', 19)
    screen = pygame.display.set_mode((750, 550))
    clock = pygame.time.Clock()
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    time.sleep(5)
    global globalSound
    globalSound = soundEffect
    print(globalSound)
    # 1 = Red
    # 2 = Orange
    # 3 = White
    # 4 = Yellow
    # 5 = Green
    # 6 = blue
    pygame.mixer.music.load("effects/targetGameStarted.mp3")
    pygame.mixer.music.play(0)
    time.sleep(5)
    pygame.display.set_caption("Target Game")
    rand = random.sample(range(6), 6)
    count = 0
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    print(rand)
    client.loop_start()
    while (count < 6):
        targetFlag = ((rand[count])+1)
        print(rand)
        print("Target: " + str(targetFlag))
        setHit(False)
        time.sleep(1)
        if (targetFlag == 1):
            pygame.mixer.music.load("effects/targetRed.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameR")
        elif (targetFlag == 2):
            pygame.mixer.music.load("effects/targetOrange.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameO")
        elif (targetFlag == 3):
            pygame.mixer.music.load("effects/targetWhite.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameW")
        elif (targetFlag == 4):
            pygame.mixer.music.load("effects/targetYellow.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameY")
        elif (targetFlag == 5):
            pygame.mixer.music.load("effects/targetGreen.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameG")
        elif (targetFlag == 6):
            pygame.mixer.music.load("effects/targetBlue.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameB")
        time.sleep(1)
        while (getHit() == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    os.killpg(proc.pid, signal.SIGTERM)
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    if stopbutton.collidepoint(mouse_pos):
                        stop(proc.pid)
                        print("Done")
                        count = 9999
                        client.loop_stop()
                        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    if redFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 1):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitred")
                            time.sleep(1)

                    if whiteFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 3):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitwhite")
                            time.sleep(1)

                    if orangeFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 2):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitorange")
                            time.sleep(1)

                    if yellowFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 4):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hityellow")
                            time.sleep(1)
                    
                    if greenFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 5):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitgreen")
                            time.sleep(1)

                    if blueFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 6):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitblue")
                            time.sleep(1)

            screen.fill([0,0,0])
            refresh()
            showStop()
            pygame.display.flip()   
            clock.tick(60)
        count+=1
        setHit(False)
    time.sleep(1)
    pygame.mixer.music.load("effects/gameCompleted.mp3")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    client.loop_stop()
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()

def startKnockOutGame(playlist, soundEffect):
    font = pygame.font.Font('freesansbold.ttf', 19)
    screen = pygame.display.set_mode((750, 550))
    clock = pygame.time.Clock()
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    time.sleep(5)
    global globalSound, reds, blues
    reds = 3
    blues = 3
    globalSound = soundEffect
    print(globalSound)
    # 1 = Red
    # 2 = Orange
    # 3 = White
    # 4 = Yellow
    # 5 = Green
    # 6 = blue
    pygame.mixer.music.load("effects/knockoutGameStarted.mp3")
    pygame.mixer.music.play(0)
    pygame.display.set_caption("Knock Out Game")
    time.sleep(5)
    count = 0
    pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    time.sleep(1)
    client.loop_start()
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "knockout")
    while (count < 9000 and reds<6 and blues<6):
        count+=1
        #os.system("mosquitto_pub -h localhost -t test_channel -m " + "status")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                client.loop_stop()
                os.killpg(proc.pid, signal.SIGTERM)
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if stopbutton.collidepoint(mouse_pos):
                    stop(proc.pid)
                    print("Done")
                    client.loop_stop()
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    count = 999999999
                    client.loop_stop()

                if redFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitred")
                    time.sleep(1)

                if whiteFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitwhite")
                    time.sleep(1)
                    
                if orangeFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitorange")
                    time.sleep(1)

                if yellowFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hityellow")
                    time.sleep(1)

                if greenFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitgreen")
                    time.sleep(1)

                if blueFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitblue")
                    time.sleep(1) 

        time.sleep(0.1)
        screen.fill([0,0,0])
        refresh()
        showStop()
        pygame.display.flip()   
        clock.tick(60)
    if (blues>5):
        pygame.mixer.music.load("effects/blueWon.mp3")
    else:
        pygame.mixer.music.load("effects/redWon.mp3")
    pygame.mixer.music.play(0)
    time.sleep(2)
    pygame.mixer.music.load("effects/gameCompleted.mp3")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    client.loop_stop()
    print(proc.pid)
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()

def startCaptureGame(playlist, soundEffect):
    font = pygame.font.Font('freesansbold.ttf', 19)
    screen = pygame.display.set_mode((750, 550))
    clock = pygame.time.Clock()
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    global globalSound
    globalSound = soundEffect
    time.sleep(5)
    print(globalSound)
    # 1 = Red
    # 2 = Orange
    # 3 = White
    # 4 = Yellow
    # 5 = Green
    # 6 = blue
    pygame.mixer.music.load("effects/captureGameStarted.mp3")
    pygame.mixer.music.play(0)
    pygame.display.set_caption("Capture Game")
    time.sleep(5)
    count = 0
    pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    time.sleep(1)
    client.loop_start()
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "capture")
    while (count < 9000):
        count+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                os.killpg(proc.pid, signal.SIGTERM)
                client.loop_stop()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if stopbutton.collidepoint(mouse_pos):
                    stop(proc.pid)
                    print("Done")
                    client.loop_stop()
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    count = 99999999
                    client.loop_stop()

                if redFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitred")
                    time.sleep(1)

                if whiteFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitwhite")
                    time.sleep(1)
                    
                if orangeFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitorange")
                    time.sleep(1)

                if yellowFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hityellow")
                    time.sleep(1)

                if greenFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitgreen")
                    time.sleep(1)

                if blueFlagOuter.collidepoint(mouse_pos):
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitblue")
                    time.sleep(1) 

        time.sleep(0.1)
        screen.fill([0,0,0])
        refresh()
        showStop()
        pygame.display.flip()   
        clock.tick(60)
    pygame.mixer.music.load("effects/gameCompleted.mp3")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    print(proc.pid)
    client.loop_stop()
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()

def startPopupGame(playlist, soundEffect):
    font = pygame.font.Font('freesansbold.ttf', 19)
    screen = pygame.display.set_mode((750, 550))
    clock = pygame.time.Clock()
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    time.sleep(5)
    global globalSound
    globalSound = soundEffect
    print(globalSound)
    # 1 = Red
    # 2 = Orange
    # 3 = White
    # 4 = Yellow
    # 5 = Green
    # 6 = blue
    pygame.mixer.music.load("effects/popupGameStarted.mp3")
    pygame.mixer.music.play(0)
    time.sleep(5)
    pygame.display.set_caption("Popup Game")
    count = 0
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    client.loop_start()
    while (count < 10):
        targetFlag = random.randint(1,6)
        print("Target: " + str(targetFlag))
        setHit(False)
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
        time.sleep(1)
        if (targetFlag == 1):
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "popup:red")
            pulse = threading.Thread(group=None, target=pulseRed, name=None)
            pulse.start()
        elif (targetFlag == 2):
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "popup:orange")
            pulse = threading.Thread(group=None, target=pulseOrange, name=None)
            pulse.start()
        elif (targetFlag == 3):
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "popup:white")
            pulse = threading.Thread(group=None, target=pulseWhite, name=None)
            pulse.start()
        elif (targetFlag == 4):
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "popup:yellow")
            pulse = threading.Thread(group=None, target=pulseYellow, name=None)
            pulse.start()
        elif (targetFlag == 5):
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "popup:green")
            pulse = threading.Thread(group=None, target=pulseGreen, name=None)
            pulse.start()
        elif (targetFlag == 6):
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "popup:blue")
            pulse = threading.Thread(group=None, target=pulseBlue, name=None)
            pulse.start()
        time.sleep(1)
        popping = 0
        while (popping < 900 and getHit() == False):
            time.sleep(0.1)
            popping += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    os.killpg(proc.pid, signal.SIGTERM)
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    if stopbutton.collidepoint(mouse_pos):
                        stop(proc.pid)
                        print("Done")
                        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                        count = 999999
                        popping = 999999999
                        client.loop_stop()
                    if redFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 1):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitred")
                            setHit(True)
                            pulse.join()
                            time.sleep(1)

                    if whiteFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 3):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitwhite")
                            setHit(True)
                            pulse.join()
                            time.sleep(1)

                    if orangeFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 2):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitorange")
                            setHit(True)
                            pulse.join()
                            time.sleep(1)

                    if yellowFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 4):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hityellow")
                            setHit(True)
                            pulse.join()
                            time.sleep(1)
                    
                    
                    if greenFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 5):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitgreen")
                            setHit(True)
                            pulse.join()
                            time.sleep(1)

                    if blueFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 6):
                            os.system("mosquitto_pub -h localhost -t test_channel -m " + "hitblue")
                            setHit(True)
                            pulse.join()
                            time.sleep(1)

            screen.fill([0,0,0])
            refresh()
            showStop()
            pygame.display.flip()   
            clock.tick(60)
        pulse.join()
        count+=1
        setHit(False)
    time.sleep(1)
    pygame.mixer.music.load("effects/gameCompleted.mp3")
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    print(proc.pid)
    client.loop_stop()
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()
