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


pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 19)
screen = pygame.display.set_mode((750, 550))
clock = pygame.time.Clock()
pygame.display.set_caption("Main Menu")


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


# Load the main Menu
def main():

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

        pygame.display.flip()
        
        clock.tick(60)


main()