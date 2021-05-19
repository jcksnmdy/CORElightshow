import pygame
import time
from games import askReadyGame

def welcomeMessage():
    pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/effects/welcome.mp3")
    pygame.mixer.music.play(0)
    time.sleep(10)
    pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/effects/readyForNight.mp3")
    pygame.mixer.music.play(0)
    time.sleep(8)
    askReadyGame()
    time.sleep(5)