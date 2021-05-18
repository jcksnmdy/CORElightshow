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
import paho.mqtt.client as mqtt
from games import startTargetGame, startKnockOutGame, startCaptureGame
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht

pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/effects/welcome.mp3")
pygame.mixer.music.play(0)

mix = pygame.Rect(10, 10, 99, 39)
lights = pygame.Rect(115, 10, 99, 39)
games = pygame.Rect(220, 10, 99, 39)
control = pygame.Rect(325, 10, 109, 39)
quick = pygame.Rect(450, 10, 99, 39)

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
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Main Menu")
state = 0
# Load the main Menu
def main():
    mixText = font.render('MIX', True, black)
    lightsText = font.render('Lights', True, black)
    gamesText = font.render('Games', True, black)
    controlText = font.render('Control', True, black)
    quickText = font.render('Quick', True, black)

    while True:
        
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                checkEventMain(mouse_pos)

#        if (state == 1):
        lightsOptions()
#        elif (state == 2):
        quickOptions()
#        elif (state == 3):
        gameOptions()
#        elif (state == 4):
        controlOptions()
        pygame.draw.rect(screen, white, mix)  # draw button
        pygame.draw.rect(screen, white, lights)  # draw button
        pygame.draw.rect(screen, white, games)  # draw button
        pygame.draw.rect(screen, white, control)  # draw button
        pygame.draw.rect(screen, white, quick)  # draw button
        screen.blit(mixText, mix)
        screen.blit(lightsText, lights)
        screen.blit(gamesText, games)
        screen.blit(controlText, control)
        screen.blit(quickText, quick)
        pygame.draw.rect(screen, white, endButton)  # draw button
        screen.blit(endText, endButton)
        

        pygame.display.flip()
        
        clock.tick(60)


songName = font.render('Hit Me', True, white)
song = 1

endButton = pygame.Rect(565, 430, 159, 39)
endText = font.render('Shutdown', True, black)
sendButton = pygame.Rect(330, 410, 69, 89)
sendText = font.render('Send', True, black)

pastSong = pygame.Rect(115, 130, 45, 39)
pastSongText = font.render('<-', True, black)
nextSong = pygame.Rect(170, 130, 45, 39)
nextSongText = font.render('->', True, black)
playButton = pygame.Rect(115, 170, 100, 39)
playButtonText = font.render('Play', True, black)

pandoraButton = pygame.Rect(115, 210, 100, 39)
pandoraButtonText = font.render('Pandora', True, black)

stationText = font.render('Top 40', True, white)
station = 1
playStation = 4

pastStation = pygame.Rect(115, 290, 45, 39)
pastStationText = font.render('<-', True, black)
nextStation = pygame.Rect(170, 290, 45, 39)
nextStationText = font.render('->', True, black)

periodTitleText = font.render('Period', True, white)
periodButton = pygame.Rect(115, 370, 100, 39)
periodText = font.render('7 mins', True, black)
period = 7
playBoth = pygame.Rect(115, 410, 100, 39)
playBothText = font.render('Both', True, black)

monday = pygame.Rect(450, 50, 140, 39)
mondayText = font.render('Monday', True, black)
tuesday = pygame.Rect(450, 90, 140, 39)
tuesdayText = font.render('Tuesday', True, black)
wednesday = pygame.Rect(450, 130, 140, 39)
wednesdayText = font.render('Wednesday', True, black)
thursday = pygame.Rect(450, 170, 140, 39)
thursdayText = font.render('Thursday', True, black)
friday = pygame.Rect(450, 210, 140, 39)
fridayText = font.render('Friday', True, black)
saturday = pygame.Rect(450, 250, 140, 39)
saturdayText = font.render('Saturday', True, black)
sunday = pygame.Rect(450, 290, 140, 39)
sundayText = font.render('Sunday', True, black)



def lightsOptions():
    global songName, stationText, song, station, period, periodText, playStation
    if (song == 1):
        songName = font.render('Serious', True, white)
    elif (song == 2):
        songName = font.render('Thunderstruck', True, white)
    elif (song == 3):
        songName = font.render('Hit Me', True, white)
    elif (song == 4):
        songName = font.render('Eye of the Tiger', True, white)
    elif (song == 5):
        songName = font.render('Despacito', True, white)
    elif (song == 6):
        songName = font.render('Beat It', True, white)
    elif (song == 7):
        songName = font.render('Thriller', True, white)
    
    if (station == 1):
        stationText = font.render('Hip Hop', True, white)
        playStation = monHipHop
    elif (station == 2):
        stationText = font.render('Rock', True, white)
        playStation = tuesRock
    elif (station == 3):
        stationText = font.render('Way Back', True, white)
        playStation = wedWayBack
    elif (station == 4):
        stationText = font.render('Throwback', True, white)
        playStation = thursThrowback
    elif (station == 5):
        stationText = font.render('Top Hits', True, white)
        playStation = fridayHits
    elif (station == 6):
        stationText = font.render('Disco', True, white)
        playStation = satDisco
    elif (station == 7):
        stationText = font.render('Country', True, white)
        playStation = sunCountry
    elif (station == 8):
        stationText = font.render('Holiday', True, white)
        playStation = holiday
    elif (station == 9):
        stationText = font.render('Yacht Rock', True, white)
        playStation = yacht
    elif (station == 10):
        stationText = font.render('Micheal J', True, white)
        playStation = michealJ

    pygame.draw.rect(screen, white, pastSong)  # draw button
    pygame.draw.rect(screen, white, nextSong)  # draw button
    pygame.draw.rect(screen, white, playButton)  # draw button
    pygame.draw.rect(screen, white, pandoraButton)  # draw button
    pygame.draw.rect(screen, white, pastStation)  # draw button
    pygame.draw.rect(screen, white, nextStation)  # draw button
    pygame.draw.rect(screen, white, periodButton)  # draw button
    screen.blit(songName, (115, 90))
    screen.blit(pastSongText, pastSong)
    screen.blit(nextSongText, nextSong)
    screen.blit(playButtonText, playButton)
    screen.blit(pandoraButtonText, pandoraButton)
    screen.blit(stationText, (115, 250))
    screen.blit(pastStationText, pastStation)
    screen.blit(nextStationText, nextStation)
    screen.blit(periodTitleText, (115, 330))
    screen.blit(periodText, periodButton)
    pygame.draw.rect(screen, white, playBoth)  # draw button
    screen.blit(playBothText, playBoth)

knockButton = pygame.Rect(220, 50, 100, 39)
knockGameName = font.render('KnockOut', True, black)
targetButton = pygame.Rect(220, 90, 100, 39)
targetGameName = font.render('Target', True, black)
captureButton = pygame.Rect(220, 130, 100, 39)
captureGameName = font.render('Capture', True, black)

soundEffect = "pew"
soundButton = pygame.Rect(225, 250, 90, 39)
soundEffectText = font.render(soundEffect, True, black)

def gameOptions():
    global knockGameName, targetGameName, captureGameName, soundEffect
    soundEffectText = font.render(soundEffect, True, black)
    pygame.draw.rect(screen, white, knockButton)  # draw button
    pygame.draw.rect(screen, white, targetButton)  # draw button
    pygame.draw.rect(screen, white, captureButton)  # draw button
    screen.blit(knockGameName, knockButton)
    screen.blit(targetGameName, targetButton)
    screen.blit(captureGameName, captureButton)
    pygame.draw.rect(screen, white, soundButton)  # draw button
    screen.blit(soundEffectText, soundButton)

redT = pygame.Rect(325, 50, 100, 39)
redTtext = font.render('Red', True, black)
oraT = pygame.Rect(325, 90, 100, 39)
oraTtext = font.render('Orange', True, black)
yelT = pygame.Rect(325, 130, 100, 39)
yelTtext = font.render('Yellow', True, black)
bluT = pygame.Rect(325, 170, 100, 39)
bluTtext = font.render('Blue', True, black)
greT = pygame.Rect(325, 210, 100, 39)
greTtext = font.render('Green', True, black)
whiT = pygame.Rect(325, 250, 100, 39)
whiTtext = font.render('White', True, black)

selectedFlag = 1
selectedColor = 1
redSelector = pygame.Rect(325, 290, 39, 39)
oraSelector = pygame.Rect(365, 290, 39, 39)
yelSelector = pygame.Rect(405, 290, 39, 39)
bluSelector = pygame.Rect(325, 330, 39, 39)
greSelector = pygame.Rect(365, 330, 39, 39)
whiSelector = pygame.Rect(405, 330, 39, 39)
purSelector = pygame.Rect(325, 370, 39, 39)
pinSelector = pygame.Rect(365, 370, 39, 39)
offSelector = pygame.Rect(405, 370, 39, 39)

def controlOptions():
    global knockGameName, targetGameName, captureGameName, selectedColor, selectedFlag
    if selectedFlag == "red":
        pygame.draw.rect(screen, white, redT)  # draw button
    else:
        pygame.draw.rect(screen, grey, redT)  # draw button
    if selectedFlag == "orange":
        pygame.draw.rect(screen, white, oraT)  # draw button
    else:
        pygame.draw.rect(screen, grey, oraT)  # draw button
    if selectedFlag == "yellow":
        pygame.draw.rect(screen, white, yelT)  # draw button
    else:
        pygame.draw.rect(screen, grey, yelT)  # draw button
    if selectedFlag == "blue":
        pygame.draw.rect(screen, white, bluT)  # draw button
    else:
        pygame.draw.rect(screen, grey, bluT)  # draw button
    if selectedFlag == "green":
        pygame.draw.rect(screen, white, greT)  # draw button
    else:
        pygame.draw.rect(screen, grey, greT)  # draw button
    if selectedFlag == "white":
        pygame.draw.rect(screen, white, whiT)  # draw button
    else:
        pygame.draw.rect(screen, grey, whiT)  # draw button

    if selectedColor == 1:
        pygame.draw.rect(screen, red, redSelector)  # draw button
    else:
        pygame.draw.rect(screen, darkred, redSelector)  # draw button
    if selectedColor == 2:
        pygame.draw.rect(screen, orange, oraSelector)  # draw button
    else:
        pygame.draw.rect(screen, darkorange, oraSelector)  # draw button
    if selectedColor == 3:
        pygame.draw.rect(screen, yellow, yelSelector)  # draw button
    else:
        pygame.draw.rect(screen, darkyellow, yelSelector)  # draw button
    if selectedColor == 4:
        pygame.draw.rect(screen, blue, bluSelector)  # draw button
    else:
        pygame.draw.rect(screen, darkblue, bluSelector)  # draw button
    if selectedColor == 5:
        pygame.draw.rect(screen, green, greSelector)  # draw button
    else:
        pygame.draw.rect(screen, darkgreen, greSelector)  # draw button
    if selectedColor == 6:
        pygame.draw.rect(screen, white, whiSelector)  # draw button
    else:
        pygame.draw.rect(screen, grey, whiSelector)  # draw button
    if selectedColor == 7:
        pygame.draw.rect(screen, (128, 0, 128), purSelector)  # draw button
    else:
        pygame.draw.rect(screen, (64,0,64), purSelector)  # draw button
    if selectedColor == 8:
        pygame.draw.rect(screen, (255, 192, 203), pinSelector)  # draw button
    else:
        pygame.draw.rect(screen, (128,98,100), pinSelector)  # draw button
    if selectedColor == 9:
        pygame.draw.rect(screen, (94,94,94), offSelector)  # draw button
    else:
        pygame.draw.rect(screen, (64,64,64), offSelector)  # draw button
    pygame.draw.rect(screen, white, sendButton)  # draw button
    screen.blit(sendText, sendButton)
    screen.blit(oraTtext, oraT)
    screen.blit(bluTtext, bluT)
    screen.blit(yelTtext, yelT)
    screen.blit(greTtext, greT)
    screen.blit(whiTtext, whiT)
    screen.blit(redTtext, redT)
    

def quickOptions():
    pygame.draw.rect(screen, white, monday)  # draw button
    screen.blit(mondayText, monday)
    pygame.draw.rect(screen, white, tuesday)  # draw button
    screen.blit(tuesdayText, tuesday)
    pygame.draw.rect(screen, white, wednesday)  # draw button
    screen.blit(wednesdayText, wednesday)
    pygame.draw.rect(screen, white, thursday)  # draw button
    screen.blit(thursdayText, thursday)
    pygame.draw.rect(screen, white, friday)  # draw button
    screen.blit(fridayText, friday)
    pygame.draw.rect(screen, white, saturday)  # draw button
    screen.blit(saturdayText, saturday)
    pygame.draw.rect(screen, white, sunday)  # draw button
    screen.blit(sundayText, sunday)

def checkEventMain(mouse_pos):
    global state, song, station, period, periodText, selectedColor, selectedFlag, soundEffect, playStation
    if soundButton.collidepoint(mouse_pos):
        if (soundEffect == "pew"):
            soundEffect = "ka-ching"
        elif (soundEffect == "ka-ching"):
            soundEffect = "shatter"
        else:
            soundEffect = "pew"
    if redT.collidepoint(mouse_pos):
        selectedFlag = "red"

    if oraT.collidepoint(mouse_pos):
        selectedFlag = "orange"

    if yelT.collidepoint(mouse_pos):
        selectedFlag = "yellow"

    if bluT.collidepoint(mouse_pos):
        selectedFlag = "blue"

    if greT.collidepoint(mouse_pos):
        selectedFlag = "green"

    if whiT.collidepoint(mouse_pos):
        selectedFlag = "white"
    
    if redSelector.collidepoint(mouse_pos):
        selectedColor = 1

    if oraSelector.collidepoint(mouse_pos):
        selectedColor = 2

    if yelSelector.collidepoint(mouse_pos):
        selectedColor = 3

    if bluSelector.collidepoint(mouse_pos):
        selectedColor = 4

    if greSelector.collidepoint(mouse_pos):
        selectedColor = 5

    if whiSelector.collidepoint(mouse_pos):
        selectedColor = 6

    if purSelector.collidepoint(mouse_pos):
        selectedColor = 7

    if pinSelector.collidepoint(mouse_pos):
        selectedColor = 8

    if offSelector.collidepoint(mouse_pos):
        selectedColor = 9

    if playButton.collidepoint(mouse_pos):
        playMusic.playSong([song-1], 0)

    if pandoraButton.collidepoint(mouse_pos):
        playMusic.playPandora(playStation, period, soundEffect)

    if playBoth.collidepoint(mouse_pos):
        playMusic.play(playStation, period, soundEffect)
    if mix.collidepoint(mouse_pos):
        print("MIX: " + soundEffect)
        startTargetGame(fridayHits, soundEffect)
                        
    if lights.collidepoint(mouse_pos):
        if (state!=1):
            state = 1
            print("lightsOptions")
        else:
            state = 0

    if games.collidepoint(mouse_pos):
        if (state!=3):
            state = 3
            print("game option")
        else:
            state = 0


    if control.collidepoint(mouse_pos):
        if (state!=4):
            state = 4
            print("Control option")
        else:
            state = 0

    if quick.collidepoint(mouse_pos):
        if (state!=2):
            state = 2
        else:
            state = 0
    if nextSong.collidepoint(mouse_pos):
        if (song < numSongs):
            song+=1
            print(song)

    if pastSong.collidepoint(mouse_pos):
        if (song > 1):
            song-=1
            print(song)

    if nextStation.collidepoint(mouse_pos):
        if (station < numStations):
            station+=1
            print(playStation)

    if pastStation.collidepoint(mouse_pos):
        if (station > 0):
            station-=1
            print(playStation)
    
    if sendButton.collidepoint(mouse_pos):
        os.system("mosquitto_pub -h localhost -t test_channel -m " + str(selectedFlag) + str(selectedColor))

    if periodButton.collidepoint(mouse_pos):
        if (period == 7):
            period = 11
            periodText = font.render('11 mins', True, black)
        elif (period == 11):
            period = 15
            periodText = font.render('15 mins', True, black)
        elif (period == 15):
            period = 30
            periodText = font.render('30 mins', True, black)
        elif (period == 30):
            period = 3
            periodText = font.render('3 mins', True, black)
        elif (period == 3):
            period = 0
            periodText = font.render('0 mins', True, black)
        else:
            period = 7
            periodText = font.render('7 mins', True, black)
    if endButton.collidepoint(mouse_pos):
        os.system("mosquitto_pub -h localhost -t test_channel -m " + "shutdown")
    
    if knockButton.collidepoint(mouse_pos):
        print("Knockout")
        startKnockOutGame(playStation, soundEffect)
    if targetButton.collidepoint(mouse_pos):
        print("Target")
        startTargetGame(playStation, soundEffect)
    if captureButton.collidepoint(mouse_pos):
        print("Capture")
        startCaptureGame(playStation, soundEffect)
    
    if sunday.collidepoint(mouse_pos):
        playMusic.play(sunCountry, period, soundEffect)

    if monday.collidepoint(mouse_pos):
        playMusic.play(monHipHop, period, soundEffect)

    if tuesday.collidepoint(mouse_pos):
        playMusic.play(tuesRock, period, soundEffect)

    if wednesday.collidepoint(mouse_pos):
        playMusic.play(wedWayBack, period, soundEffect)

    if thursday.collidepoint(mouse_pos):
        playMusic.play(thursThrowback, period, soundEffect)

    if friday.collidepoint(mouse_pos):
        playMusic.play(fridayHits, period, soundEffect)
    
    if saturday.collidepoint(mouse_pos):
        playMusic.play(satDisco, period, soundEffect)

main()