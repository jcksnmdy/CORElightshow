import pygame
import os
import time
import random
import subprocess
import signal
import threading
import playMusic
import sys
from broadcastDisplay import pulseRed, pulseOrange, pulseWhite, pulseYellow, pulseGreen, pulseBlue, sparkleRed, whiteFlagOuter, redFlagOuter, orangeFlagOuter, blueFlagOuter, greenFlagOuter, yellowFlagOuter, setHit, getHit, refresh

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


def startTargetGame(playlist, soundEffect, targetFlag):
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
    pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
    pygame.mixer.music.set_volume(1.0)
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    count = 0
    print(rand)
    print("Removing " + str(targetFlag))
    rand.remove(targetFlag-1)
    print(rand)
    while (count < 6):
        print("Target: " + str(targetFlag))
        setHit(False)
        if (targetFlag == 1):
            pygame.mixer.music.load("effects/targetRed.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseRed, name=None)
            pulse.start()
        elif (targetFlag == 2):
            pygame.mixer.music.load("effects/targetOrange.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseOrange, name=None)
            pulse.start()
        elif (targetFlag == 3):
            pygame.mixer.music.load("effects/targetWhite.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseWhite, name=None)
            pulse.start()
        elif (targetFlag == 4):
            pygame.mixer.music.load("effects/targetYellow.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseYellow, name=None)
            pulse.start()
        elif (targetFlag == 5):
            pygame.mixer.music.load("effects/targetGreen.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseGreen, name=None)
            pulse.start()
        elif (targetFlag == 6):
            pygame.mixer.music.load("effects/targetBlue.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseBlue, name=None)
            pulse.start()
        time.sleep(1)
        while (getHit() == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    os.killpg(proc.pid, signal.SIGTERM)
                    pygame.quit()
                    main()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position

                    if redFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 1):
                            setHit(True)
                            pulse.join()
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            sparkle = threading.Thread(group=None, target=sparkleRed, name=None)
                            sparkle.start()
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informRed.mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(2.5)


                    if whiteFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 3):
                            setHit(True)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informWhite.mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(2.5)
                    
                    if orangeFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 2):
                            setHit(True)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informOrange.mp3")
                            pygame.mixer.music.play(0)
                            
                            time.sleep(2.5)

                    if yellowFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 4):
                            setHit(True)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informYellow.mp3")
                            pygame.mixer.music.play(0)

                            time.sleep(2.5)
                    
                    
                    if greenFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 5):
                            setHit(True)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informGreen.mp3")
                            pygame.mixer.music.play(0)
                            
                            time.sleep(2.5)

                    if blueFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 6):
                            setHit(True)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informBlue.mp3")
                            pygame.mixer.music.play(0)
                        
                            time.sleep(2.5)   

                    if blueFlagOuter.collidepoint(mouse_pos):
                        stop()         

            screen.fill([0,0,0])
            refresh()
            pygame.display.flip()   
            clock.tick(60)
        sparkle.join()
        pulse.join()
        targetFlag = ((rand[count-1])+1)
        print(rand)
        setHit(True)
        count+=1
    pygame.mixer.music.load("effects/gameCompleted.mp3")
    pygame.mixer.music.play(0)
    time.sleep(1.5)
    pygame.mixer.music.stop()
    print(proc.pid)
    os.killpg(proc.pid, signal.SIGTERM)
    pygame.mixer.music.stop()
    pygame.quit()
    main()
