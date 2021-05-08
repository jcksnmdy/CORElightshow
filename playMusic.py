import pandas as pd
import pygame
import os
import time
import random
import subprocess
import signal
import threading
import pygame_widgets
from broadcastDisplay import showTargets, stopbutton, showStop
import sys
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht, path

def playSong(rand, count):
    os.system("mosquitto_pub -h localhost -t test_channel -m " + str(rand[count]+1))
    print("Programmed song playing. Programmed song count: " + str(count+1) + ". Song index: " + str(rand[count]+1) + "")
    i = 5
    allInfo = pd.read_excel(path + "/flagCode/song" + str(rand[count]+1) + ".xlsx")
    pygame.mixer.music.load(path + "/songs/song" + str(rand[count]+1) + ".mp3")
    pygame.mixer.music.play(0)
    while (i < len(allInfo)):
        showTargets(rand, count, i)
        i+=7
    pygame.mixer.music.stop()

def playPandora(playlist, delay):
    print("playing pandora station: " + str(playlist))
    proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
    print(proc.pid)
    timer = 0
    while timer < delay*60:
        time.sleep(1)
        timer+=1
        showStop()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if stopbutton.collidepoint(mouse_pos):
                    stop(proc.pid)
                    print("Done")
                    break

def play(playlist, delay):
    count = numSongs-1
    rand = random.sample(range(numSongs), numSongs)
    print(rand)
    while count < numSongs:
        playSong(rand, count)
        count+=1
        pygame.mixer.music.stop()
        playPandora(playlist, delay)
    print("Yep Done")

def stop(id):
    pygame.mixer.music.stop()
    pygame.mixer.music.stop()
    os.killpg(id, signal.SIGTERM)
    pygame.quit()