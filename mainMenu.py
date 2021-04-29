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
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht

mix = pygame.Rect(10, 10, 99, 39)
lights = pygame.Rect(115, 10, 99, 39)
games = pygame.Rect(220, 10, 99, 39)
control = pygame.Rect(325, 10, 109, 39)
quick = pygame.Rect(440, 10, 99, 39)

red = (255,0,0)
orange = (255,128,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)
white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)
pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 28)
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

        if (state == 1):
            lightsOptions(mouse_pos)
        elif (state == 2):
            quickOptions(mouse_pos)
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
        
        

        pygame.display.flip()
        
        clock.tick(60)


songName = font.render('Hit Me', True, white)
song = 1

pastSong = pygame.Rect(115, 130, 69, 39)
pastSongText = font.render('Last', True, black)
nextSong = pygame.Rect(190, 130, 69, 39)
nextSongText = font.render('Next', True, black)
playButton = pygame.Rect(115, 170, 144, 39)
playButtonText = font.render('Play', True, black)

pandoraButton = pygame.Rect(115, 210, 144, 39)
pandoraButtonText = font.render('Pandora', True, black)

stationText = font.render('Top 40', True, white)
station = 1
playStation = 4

pastStation = pygame.Rect(115, 290, 69, 39)
pastStationText = font.render('Last', True, black)
nextStation = pygame.Rect(190, 290, 69, 39)
nextStationText = font.render('Next', True, black)

periodTitleText = font.render('Period', True, white)
periodButton = pygame.Rect(115, 370, 144, 39)
periodText = font.render('7 mins', True, black)
period = 7
playBoth = pygame.Rect(115, 410, 144, 39)
playBothText = font.render('Play Both', True, black)

monday = pygame.Rect(440, 50, 150, 39)
mondayText = font.render('Monday', True, black)
tuesday = pygame.Rect(440, 90, 150, 39)
tuesdayText = font.render('Tuesday', True, black)
wednesday = pygame.Rect(440, 130, 150, 39)
wednesdayText = font.render('Wednesday', True, black)
thursday = pygame.Rect(440, 170, 150, 39)
thursdayText = font.render('Thursday', True, black)
friday = pygame.Rect(440, 210, 150, 39)
fridayText = font.render('Friday', True, black)
saturday = pygame.Rect(440, 250, 150, 39)
saturdayText = font.render('Saturday', True, black)
sunday = pygame.Rect(440, 290, 150, 39)
sundayText = font.render('Sunday', True, black)



def lightsOptions(mouse_pos):
    global songName, stationText, song, station, period, periodText
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

def quickOptions(mouse_pos):
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
    global state, song, station, period, periodText
    if mix.collidepoint(mouse_pos):
        print("System Unavailable")
                        
    if lights.collidepoint(mouse_pos):
        if (state!=1):
            state = 1
        else:
            state = 0

    if games.collidepoint(mouse_pos):
        #targetGameSetup()
        print("System Unavailable")

    if control.collidepoint(mouse_pos):
        print("System Unavailable")

    if quick.collidepoint(mouse_pos):
        if (state!=2):
            state = 2
        else:
            state = 0


    if nextSong.collidepoint(mouse_pos):
        if (song < numSongs):
            song+=1

    if pastSong.collidepoint(mouse_pos):
        if (song > 1):
            song-=1

    if nextStation.collidepoint(mouse_pos):
        if (station < numStations):
            station+=1

    if pastStation.collidepoint(mouse_pos):
        if (station > 0):
            station-=1

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
    
    if sunday.collidepoint(mouse_pos):
        playMusic.play(sunCountry)

    if monday.collidepoint(mouse_pos):
        playMusic.play(monHipHop)

    if tuesday.collidepoint(mouse_pos):
        playMusic.play(tuesRock)

    if wednesday.collidepoint(mouse_pos):
        playMusic.play(wedWayBack)

    if thursday.collidepoint(mouse_pos):
        playMusic.play(thursThrowback)

    if friday.collidepoint(mouse_pos):
        playMusic.play(fridayHits)
    
    if saturday.collidepoint(mouse_pos):
        playMusic.play(satDisco)

main()