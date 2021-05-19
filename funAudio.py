import pygame
import time
from games import askReadyGame

def welcomeMessage():
    pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/effects/welcome.mp3")
    pygame.mixer.music.play(0)
    time.sleep(4)
    askReadyGame()
    time.sleep(5)