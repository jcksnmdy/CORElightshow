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
from broadcastDisplay import pulseRed, pulseOrange, pulseWhite, pulseYellow, pulseGreen, pulseBlue, sparkleRed, whiteFlagOuter, redFlagOuter, orangeFlagOuter, blueFlagOuter, greenFlagOuter, yellowFlagOuter, setHit, getHit, refresh, showStop, stopbutton, redFlagLeftOrig, orangeFlagLeftOrig, whiteFlagLeftOrig, yellowFlagLeftOrig, greenFlagLeftOrig, blueFlagLeftOrig, setRedFlagSame, setOrangeFlagSame, setWhiteFlagSame, setGreenFlagSame, setBlueFlagSame, setYellowFlagSame
from playMusic import stop

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

globalSound = "pew"
MQTT_SERVER = "192.168.1.119"
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
    global reds, blues, red, blue, black, grey
    print(msg.topic+" "+str(msg.payload))
    if("hit" in str(msg.payload)):
        print("hittt")
        setHit(True)
        pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/effects/" + globalSound + ".mp3")
        pygame.mixer.music.play(0)
        time.sleep(1)
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
        red+=1
        blue-=1
        setBlueFlagSame(red, blueFlagLeftOrig)
    if ("whiteStatus:rK" in str(msg.payload)):
        red+=1
        blue-=1
        setWhiteFlagSame(red, whiteFlagLeftOrig)
    if ("redStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setRedFlagSame(blue, redFlagLeftOrig)
    if ("orangeStatus:bK" in str(msg.payload)):
        reds-=1
        blues+=1
        setOrangeFlagSame(blue, OrangeFlagLeftOrig)
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
    time.sleep(1)
    
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

def startTargetGame(playlist, soundEffect, targetFlag):
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
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
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Target Game")
    pygame.mixer.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    rand = random.sample(range(6), 6)
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    count = 0
    print(rand)
    client.loop_start()
    while (count < 6):
        print("Target: " + str(targetFlag))
        setHit(False)
        if (targetFlag == 1):
            pygame.mixer.music.load("effects/targetRed.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameR")
            pulse = threading.Thread(group=None, target=pulseRed, name=None)
            pulse.start()
        elif (targetFlag == 2):
            pygame.mixer.music.load("effects/targetOrange.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameO")
            pulse = threading.Thread(group=None, target=pulseOrange, name=None)
            pulse.start()
        elif (targetFlag == 3):
            pygame.mixer.music.load("effects/targetWhite.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameW")
            pulse = threading.Thread(group=None, target=pulseWhite, name=None)
            pulse.start()
        elif (targetFlag == 4):
            pygame.mixer.music.load("effects/targetYellow.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameY")
            pulse = threading.Thread(group=None, target=pulseYellow, name=None)
            pulse.start()
        elif (targetFlag == 5):
            pygame.mixer.music.load("effects/targetGreen.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameG")
            pulse = threading.Thread(group=None, target=pulseGreen, name=None)
            pulse.start()
        elif (targetFlag == 6):
            pygame.mixer.music.load("effects/targetBlue.mp3")
            pygame.mixer.music.play(0)
            os.system("mosquitto_pub -h localhost -t test_channel -m " + "targetGameB")
            pulse = threading.Thread(group=None, target=pulseBlue, name=None)
            pulse.start()
        time.sleep(1)
        while (getHit() == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    os.killpg(proc.pid, signal.SIGTERM)
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    pygame.quit()
                    main()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    if stopbutton.collidepoint(mouse_pos):
                        stop(proc.pid)
                        print("Done")
                        os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                        break
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
        if (count<len(rand)):
            targetFlag = ((rand[count-1])+1)
        print(rand)
        setHit(True)
    pygame.mixer.music.load("effects/gameCompleted.mp3")
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    print(proc.pid)
    client.loop_stop()
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()
    pygame.quit()
    main()

def startKnockOutGame(playlist, soundEffect):
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
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
    time.sleep(5)
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Knockout Game")
    pygame.mixer.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    count = 0
    pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)

    client.loop_start()
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "knockout")
    while (count < 9000):
        count+=1
        #os.system("mosquitto_pub -h localhost -t test_channel -m " + "status")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                client.loop_stop()
                os.killpg(proc.pid, signal.SIGTERM)
                pygame.quit()
                main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if stopbutton.collidepoint(mouse_pos):
                    stop(proc.pid)
                    print("Done")
                    client.loop_stop()
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    break

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
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    client.loop_stop()
    print(proc.pid)
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()
    pygame.quit()
    main()

def startCaptureGame(playlist, soundEffect):
    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
    global globalSound
    globalSound = soundEffect
    print(globalSound)
    # 1 = Red
    # 2 = Orange
    # 3 = White
    # 4 = Yellow
    # 5 = Green
    # 6 = blue
    pygame.mixer.music.load("effects/captureGameStarted.mp3")
    pygame.mixer.music.play(0)
    time.sleep(5)
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Knockout Game")
    pygame.mixer.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    count = 0
    pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)

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
                main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if stopbutton.collidepoint(mouse_pos):
                    stop(proc.pid)
                    print("Done")
                    client.loop_stop()
                    os.system("mosquitto_pub -h localhost -t test_channel -m " + "stop")
                    break

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
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    print(proc.pid)
    client.loop_stop()
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()
    pygame.quit()
    main()
