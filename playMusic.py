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

numInPlaylist = 1

def play(playlist):
    count = numInPlaylist-1
    rand = random.sample(range(numInPlaylist), numInPlaylist)
    print(rand)
    while count < numInPlaylist:
        print("Programmed song playing. Programmed song count: " + str(count+1) + ". Song index: " + str(rand[count]+1) + "")
        i = 5
        redInfo = pd.read_excel("songs/song" + str(rand[count]+1) + "Red.xlsx")
        pygame.mixer.music.load("songs/song" + str(rand[count]+1) + ".mp3")
        #df = pd.read_excel("/home/pi/Desktop/coreLightShow/songs/song" + str(rand[count]+1) + ".xlsx")
        #pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/songs/song" + str(rand[count]+1) + ".mp3")
        pygame.mixer.music.play(0)
        while (i < len(redInfo)):
            showTargets(rand, count, i)
            i+=1

        count+=1
        pygame.mixer.music.stop()
        print("playing pandora station: " + str(playlist))
        proc = subprocess.Popen('pydora -t {0}'.format(playlist), shell=True, preexec_fn=os.setsid)
        print(proc.pid)
        timer = 0
        while timer < 43200:
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
    print("Yep Done")

def stop(id):
    pygame.mixer.music.stop()
    pygame.mixer.music.stop()
    os.killpg(id, signal.SIGTERM)
    pygame.quit()