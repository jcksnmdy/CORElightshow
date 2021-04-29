import pandas as pd
import pygame
import os
import time
import random
import subprocess
import signal
import threading
import pygame_widgets
import sys
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht, path

pygame.init()
pygame.font.init()
pygame.display.set_caption("Player")
font = pygame.font.Font('freesansbold.ttf', 28)
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

red = (255,0,0)
orange = (255,128,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)
white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)

## Left
redFlagColorLeft = red
orangeFlagColorLeft = orange
whiteFlagColorLeft = white
yellowFlagColorLeft = yellow
greenFlagColorLeft = green
blueFlagColorLeft = blue
## MIDDLE
redFlagColorMiddle = red
orangeFlagColorMiddle = orange
whiteFlagColorMiddle = white
yellowFlagColorMiddle = yellow
greenFlagColorMiddle = green
blueFlagColorMiddle = blue
## Right
redFlagColorRight = red
orangeFlagColorRight = orange
whiteFlagColorRight = white
yellowFlagColorRight = yellow
greenFlagColorRight = green
blueFlagColorRight = blue

## Left
redFlagLeftOrig = (120, 330, 39, 39)
orangeFlagLeftOrig = (450, 280, 39, 39)
whiteFlagLeftOrig = (340, 190, 39, 39)
yellowFlagLeftOrig = (150, 220, 39, 39)
greenFlagLeftOrig = (240, 160, 39, 39)
blueFlagLeftOrig = (470, 100, 39, 39)

redFlagLeft = pygame.Rect(redFlagLeftOrig)
orangeFlagLeft = pygame.Rect(orangeFlagLeftOrig)
whiteFlagLeft = pygame.Rect(whiteFlagLeftOrig)
yellowFlagLeft = pygame.Rect(yellowFlagLeftOrig)
greenFlagLeft = pygame.Rect(greenFlagLeftOrig)
blueFlagLeft = pygame.Rect(blueFlagLeftOrig)
##MIDDLE
redFlagMiddleOrig = (110, 320, 59, 59)
orangeFlagMiddleOrig = (430, 270, 59, 59)
whiteFlagMiddleOrig = (330, 180, 59, 59)
yellowFlagMiddleOrig = (140, 210, 59, 59)
greenFlagMiddleOrig = (230, 150, 59, 59)
blueFlagMiddleOrig = (460, 90, 59, 59)

redFlagMiddle = pygame.Rect(redFlagMiddleOrig)
orangeFlagMiddle = pygame.Rect(orangeFlagMiddleOrig)
whiteFlagMiddle = pygame.Rect(whiteFlagMiddleOrig)
yellowFlagMiddle = pygame.Rect(yellowFlagMiddleOrig)
greenFlagMiddle = pygame.Rect(greenFlagMiddleOrig)
blueFlagMiddle = pygame.Rect(blueFlagMiddleOrig)
##Right
redFlagRightOrig = (100, 310, 79, 79)
orangeFlagRightOrig = (430, 260, 79, 79)
whiteFlagRightOrig = (320, 170, 79, 79)
yellowFlagRightOrig = (130, 200, 79, 79)
greenFlagRightOrig = (220, 140, 79, 79)
blueFlagRightOrig = (450, 80, 79, 79)

redFlagRight = pygame.Rect(redFlagRightOrig)
orangeFlagRight = pygame.Rect(orangeFlagRightOrig)
whiteFlagRight = pygame.Rect(whiteFlagRightOrig)
yellowFlagRight = pygame.Rect(yellowFlagRightOrig)
greenFlagRight = pygame.Rect(greenFlagRightOrig)
blueFlagRight = pygame.Rect(blueFlagRightOrig)

def sparkleRed():
    print("Sparkling")
    setRedFlag(red, grey, grey, redFlagLeftOrig)
    time.sleep(0.2)
    setRedFlag(grey, red, grey, redFlagLeftOrig)
    time.sleep(0.2)
    setRedFlag(red, grey, grey, redFlagLeftOrig)
    time.sleep(0.2)
    setRedFlag(grey, grey, red, redFlagLeftOrig)
    time.sleep(0.2)
    setRedFlag(red, grey, grey, redFlagLeftOrig)
    time.sleep(0.2)
    setRedFlag(grey, grey, red, redFlagLeftOrig)
    time.sleep(0.2)
    setRedFlag(grey, red, grey, redFlagLeftOrig)
    time.sleep(0.2)

def pulseRed():
    while (hit == False):
        setRedFlag(red, grey, grey, redFlagLeftOrig)
        time.sleep(0.2)
        setRedFlag(grey, red, grey, redFlagLeftOrig)
        time.sleep(0.1)
        setRedFlag(grey, grey, red, redFlagLeftOrig)
        time.sleep(0.09)
        setRedFlag(grey, grey, grey, redFlagLeftOrig)
        time.sleep(1)
    
def pulseOrange():
    while (hit == False):
        setOrangeFlag(orange, grey, grey, orangeFlagLeftOrig)
        time.sleep(0.2)
        setOrangeFlag(grey, orange, grey, orangeFlagLeftOrig)
        time.sleep(0.1)
        setOrangeFlag(grey, grey, orange, orangeFlagLeftOrig)
        time.sleep(0.09)
        setOrangeFlag(grey, grey, grey, orangeFlagLeftOrig)
        time.sleep(1)

def pulseWhite():
    while (hit == False):
        setWhiteFlag(white, grey, grey, whiteFlagLeftOrig)
        time.sleep(0.2)
        setWhiteFlag(grey, white, grey, whiteFlagLeftOrig)
        time.sleep(0.1)
        setWhiteFlag(grey, grey, white, whiteFlagLeftOrig)
        time.sleep(0.09)
        setWhiteFlag(grey, grey, grey, whiteFlagLeftOrig)
        time.sleep(1)

def pulseYellow():
    while (hit == False):
        setYellowFlag(yellow, grey, grey, yellowFlagLeftOrig)
        time.sleep(0.2)
        setYellowFlag(grey, yellow, grey, yellowFlagLeftOrig)
        time.sleep(0.1)
        setYellowFlag(grey, grey, yellow, yellowFlagLeftOrig)
        time.sleep(0.09)
        setYellowFlag(grey, grey, grey, yellowFlagLeftOrig)
        time.sleep(1)

def pulseGreen():
    while (hit == False):
        setGreenFlag(green, grey, grey, greenFlagLeftOrig)
        time.sleep(0.2)
        setGreenFlag(grey, green, grey, greenFlagLeftOrig)
        time.sleep(0.1)
        setGreenFlag(grey, grey, green, greenFlagLeftOrig)
        time.sleep(0.09)
        setGreenFlag(grey, grey, grey, greenFlagLeftOrig)
        time.sleep(1)

def pulseBlue():
    while (hit == False):
        setBlueFlag(blue, grey, grey, blueFlagLeftOrig)
        time.sleep(0.2)
        setBlueFlag(grey, blue, grey, blueFlagLeftOrig)
        time.sleep(0.1)
        setBlueFlag(grey, grey, blue, blueFlagLeftOrig)
        time.sleep(0.09)
        setBlueFlag(grey, grey, grey, blueFlagLeftOrig)
        time.sleep(1)

def setRedFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    Left = space
    middle = (spaceList[0]-10,spaceList[1]-10,spaceList[2]+20,spaceList[3]+20)
    Right = (spaceList[0]-20,spaceList[1]-20,spaceList[2]+40,spaceList[3]+40)

    global redFlagColorLeft, redFlagLeft, redFlagColorMiddle, redFlagMiddle, redFlagColorRight, redFlagRight
    redFlagColorLeft = colorLeft
    redFlagLeft = pygame.Rect(Left)
    redFlagColorMiddle = colorMiddle
    redFlagMiddle = pygame.Rect(middle)
    redFlagColorRight = colorRight
    redFlagRight = pygame.Rect(Right)

def setOrangeFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    Left = space
    middle = (spaceList[0]-10,spaceList[1]-10,spaceList[2]+20,spaceList[3]+20)
    Right = (spaceList[0]-20,spaceList[1]-20,spaceList[2]+40,spaceList[3]+40)

    global orangeFlagColorLeft, orangeFlagLeft, orangeFlagColorMiddle, orangeFlagMiddle, orangeFlagColorRight, orangeFlagRight
    orangeFlagColorLeft = colorLeft
    orangeFlagLeft = pygame.Rect(Left)
    orangeFlagColorMiddle = colorMiddle
    orangeFlagMiddle = pygame.Rect(middle)
    orangeFlagColorRight = colorRight
    orangeFlagRight = pygame.Rect(Right)

def setWhiteFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    Left = space
    middle = (spaceList[0]-10,spaceList[1]-10,spaceList[2]+20,spaceList[3]+20)
    Right = (spaceList[0]-20,spaceList[1]-20,spaceList[2]+40,spaceList[3]+40)

    global whiteFlagColorLeft, whiteFlagLeft, whiteFlagColorMiddle, whiteFlagMiddle, whiteFlagColorRight, whiteFlagRight
    whiteFlagColorLeft = colorLeft
    whiteFlagLeft = pygame.Rect(Left)
    whiteFlagColorMiddle = colorMiddle
    whiteFlagMiddle = pygame.Rect(middle)
    whiteFlagColorRight = colorRight
    whiteFlagRight = pygame.Rect(Right)

def setYellowFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    Left = space
    middle = (spaceList[0]-10,spaceList[1]-10,spaceList[2]+20,spaceList[3]+20)
    Right = (spaceList[0]-20,spaceList[1]-20,spaceList[2]+40,spaceList[3]+40)

    global yellowFlagColorLeft, yellowFlagLeft, yellowFlagColorMiddle, yellowFlagMiddle, yellowFlagColorRight, yellowFlagRight
    yellowFlagColorLeft = colorLeft
    yellowFlagLeft = pygame.Rect(Left)
    yellowFlagColorMiddle = colorMiddle
    yellowFlagMiddle = pygame.Rect(middle)
    yellowFlagColorRight = colorRight
    yellowFlagRight = pygame.Rect(Right)

def setGreenFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    Left = space
    middle = (spaceList[0]-10,spaceList[1]-10,spaceList[2]+20,spaceList[3]+20)
    Right = (spaceList[0]-20,spaceList[1]-20,spaceList[2]+40,spaceList[3]+40)

    global greenFlagColorLeft, greenFlagLeft, greenFlagColorMiddle, greenFlagMiddle, greenFlagColorRight, greenFlagRight
    greenFlagColorLeft = colorLeft
    greenFlagLeft = pygame.Rect(Left)
    greenFlagColorMiddle = colorMiddle
    greenFlagMiddle = pygame.Rect(middle)
    greenFlagColorRight = colorRight
    greenFlagRight = pygame.Rect(Right)

def setBlueFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    Left = space
    middle = (spaceList[0]-10,spaceList[1]-10,spaceList[2]+20,spaceList[3]+20)
    Right = (spaceList[0]-20,spaceList[1]-20,spaceList[2]+40,spaceList[3]+40)

    global blueFlagColorLeft, blueFlagLeft, blueFlagColorMiddle, blueFlagMiddle, blueFlagColorRight, blueFlagRight
    blueFlagColorLeft = colorLeft
    blueFlagLeft = pygame.Rect(Left)
    blueFlagColorMiddle = colorMiddle
    blueFlagMiddle = pygame.Rect(middle)
    blueFlagColorRight = colorRight
    blueFlagRight = pygame.Rect(Right)

def setRedFlagSame(color, space):
    setRedFlag(color, color, color, space)

def setOrangeFlagSame(color, space):
    setOrangeFlag(color, color, color, space)

def setWhiteFlagSame(color, space):
    setWhiteFlag(color, color, color, space)

def setYellowFlagSame(color, space):
    setYellowFlag(color, color, color, space)

def setGreenFlagSame(color, space):
    setGreenFlag(color, color, color, space)

def setBlueFlagSame(color, space):
    setBlueFlag(color, color, color, space)

def resetAllFlags():
    setRedFlag(red, red, red,redFlagLeftOrig)
    setOrangeFlag(orange, orange, orange, orangeFlagLeftOrig)
    setWhiteFlag(white, white, white, whiteFlagLeftOrig)
    setYellowFlag(yellow, yellow, yellow, yellowFlagLeftOrig)
    setGreenFlag(green, green, green, greenFlagLeftOrig)
    setBlueFlag(blue, blue, blue, blueFlagLeftOrig)

def toTuple(before):
    print("Before: " + str(before))
    firstNum = float(before[before.find("(")+1:before.find(",")])
    secNum = float(before[before.find(",")+2:before.find(",", 7)])
    thirdNum = float(before[before.find(",", 7)+2:before.find(")")])
    returning = (firstNum, secNum, thirdNum)
    print("Returning:" + str(returning))
    return returning

def showTargets(rand, count, i):
    allInfo = pd.read_excel(path + "/flagCode/song" + str(rand[count]+1) + ".xlsx")
    screen.fill([0,0,0])
    print(len(allInfo))
    #print(str(i)+ " "+ str(toColor(df.loc[(i),'Red 1'])))
    print(toTuple(allInfo.loc[(i),'red Left']))
    setRedFlagSame(toTuple(allInfo.loc[(i),'red Left']), redFlagLeftOrig)
    setOrangeFlagSame(toTuple(allInfo.loc[(i),'orange Left']), orangeFlagLeftOrig)
    setWhiteFlagSame(toTuple(allInfo.loc[(i),'white Left']), whiteFlagLeftOrig)
    setYellowFlagSame(toTuple(allInfo.loc[(i),'yellow Left']), yellowFlagLeftOrig)
    setGreenFlagSame(toTuple(allInfo.loc[(i),'green Left']), greenFlagLeftOrig)
    setBlueFlagSame(toTuple(allInfo.loc[(i),'blue Left']), blueFlagLeftOrig)

    pygame.draw.rect(screen, redFlagColorLeft, redFlagLeft)  # draw button
    pygame.draw.rect(screen, orangeFlagColorLeft, orangeFlagLeft)  # draw button
    pygame.draw.rect(screen, whiteFlagColorLeft, whiteFlagLeft)  # draw button
    pygame.draw.rect(screen, yellowFlagColorLeft, yellowFlagLeft)  # draw button
    pygame.draw.rect(screen, greenFlagColorLeft, greenFlagLeft)  # draw button
    pygame.draw.rect(screen, blueFlagColorLeft, blueFlagLeft)  # draw button
    pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
    pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
    pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
    pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
    pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
    pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button
    pygame.draw.rect(screen, redFlagColorRight, redFlagRight)  # draw button
    pygame.draw.rect(screen, orangeFlagColorRight, orangeFlagRight)  # draw button
    pygame.draw.rect(screen, whiteFlagColorRight, whiteFlagRight)  # draw button
    pygame.draw.rect(screen, yellowFlagColorRight, yellowFlagRight)  # draw button
    pygame.draw.rect(screen, greenFlagColorRight, greenFlagRight)  # draw button
    pygame.draw.rect(screen, blueFlagColorRight, blueFlagRight)  # draw button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()

    pygame.display.flip()   
    clock.tick(60)

def toColor(col):
    if (col == "red"):
        return red
    elif (col == "blue"):
        return blue
    elif (col == "green"):
        return green
    elif (col == "yellow"):
        return yellow
    elif (col == "white"):
        return white
    elif (col == "grey"):
        return grey
    elif (col == "orange"):
        return orange
    elif (col == "black"):
        return black
    elif (col == "[255, 0, 0]"):
        return red
    elif (col == "[0, 0, 255]"):
        return blue
    elif (col == "[0, 255, 0]"):
        return green
    elif (col == "[255, 255, 0]"):
        return yellow
    elif (col == "[255, 255, 255]"):
        return white
    elif (col == "[128, 128, 128]"):
        return grey
    elif (col == "[255, 128, 0]" or col == "[255, 168, 0]"):
        return orange
    elif (col == "[0, 0, 0]"):
        return black
stopbutton = pygame.Rect(450, 10, 50, 50)
stopText = font.render('Stop', True, black)

def showStop():
    pygame.draw.rect(screen, white, stopbutton)  # draw button
    screen.blit(stopText, stopbutton)

    pygame.display.flip()   
    clock.tick(60)