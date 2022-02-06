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
sys.path.append('/Users/s1034274/Desktop/globals')
#sys.path.append('/home/pi/Desktop/globals/')
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

#tester#######################################tester######################################
#############################################
#############################################
#tester#######################################tester######################################
#############################################
#############################################
redFlagOuter = pygame.Rect((460, 90, 39, 39))
orangeFlagOuter = pygame.Rect((460, 160, 39, 39))
whiteFlagOuter = pygame.Rect((460, 230, 39, 39))
yellowFlagOuter = pygame.Rect((460, 300, 39, 39))
greenFlagOuter = pygame.Rect((460, 370, 39, 39))
blueFlagOuter = pygame.Rect((460, 440, 39, 39))
#tester######################################
##############################################tester######################################
##############################################tester######################################
##############################################tester######################################
##############################################tester######################################
#############################################
## Left
redFlagLeftOrig = (120, 330, 19, 79)
orangeFlagLeftOrig = (450, 280, 19, 79)
whiteFlagLeftOrig = (340, 190, 19, 79)
yellowFlagLeftOrig = (150, 220, 19, 79)
greenFlagLeftOrig = (240, 160, 19, 79)
blueFlagLeftOrig = (470, 100, 19, 79)

redFlagLeft = pygame.Rect(redFlagLeftOrig)
orangeFlagLeft = pygame.Rect(orangeFlagLeftOrig)
whiteFlagLeft = pygame.Rect(whiteFlagLeftOrig)
yellowFlagLeft = pygame.Rect(yellowFlagLeftOrig)
greenFlagLeft = pygame.Rect(greenFlagLeftOrig)
blueFlagLeft = pygame.Rect(blueFlagLeftOrig)

##MIDDLE
redFlagMiddleOrig = (140, 330, 19, 79)
orangeFlagMiddleOrig = (470, 280, 19, 79)
whiteFlagMiddleOrig = (360, 190, 19, 79)
yellowFlagMiddleOrig = (170, 220, 19, 79)
greenFlagMiddleOrig = (260, 160, 19, 79)
blueFlagMiddleOrig = (490, 100, 19, 79)

redFlagMiddle = pygame.Rect(redFlagMiddleOrig)
orangeFlagMiddle = pygame.Rect(orangeFlagMiddleOrig)
whiteFlagMiddle = pygame.Rect(whiteFlagMiddleOrig)
yellowFlagMiddle = pygame.Rect(yellowFlagMiddleOrig)
greenFlagMiddle = pygame.Rect(greenFlagMiddleOrig)
blueFlagMiddle = pygame.Rect(blueFlagMiddleOrig)
##Right
redFlagRightOrig = (160, 330, 19, 79)
orangeFlagRightOrig = (490, 280, 19, 79)
whiteFlagRightOrig = (380, 190, 19, 79)
yellowFlagRightOrig = (190, 220, 19, 79)
greenFlagRightOrig = (280, 160, 19, 79)
blueFlagRightOrig = (510, 100, 19, 79)

redFlagRight = pygame.Rect(redFlagRightOrig)
orangeFlagRight = pygame.Rect(orangeFlagRightOrig)
whiteFlagRight = pygame.Rect(whiteFlagRightOrig)
yellowFlagRight = pygame.Rect(yellowFlagRightOrig)
greenFlagRight = pygame.Rect(greenFlagRightOrig)
blueFlagRight = pygame.Rect(blueFlagRightOrig)

hit = False

def setHit(status):
    global hit
    hit = status

def getHit():
    global hit
    return hit

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
    global hit
    hit = False
    while (hit == False):
        setRedFlag(red, red, red, redFlagLeftOrig)
        time.sleep(0.2)
        setRedFlag(grey, grey, grey, redFlagLeftOrig)
        time.sleep(0.1)
    
def pulseOrange():
    global hit
    hit = False
    while (hit == False):
        setOrangeFlag(orange, orange, orange, orangeFlagLeftOrig)
        time.sleep(0.2)
        setOrangeFlag(grey, grey, grey, orangeFlagLeftOrig)
        time.sleep(0.1)

def pulseWhite():
    global hit
    hit = False
    while (hit == False):
        setWhiteFlag(white, white, white, whiteFlagLeftOrig)
        time.sleep(0.2)
        setWhiteFlag(grey, grey, grey, whiteFlagLeftOrig)
        time.sleep(0.1)

def pulseYellow():
    global hit
    hit = False
    while (hit == False):
        setYellowFlag(yellow, yellow, yellow, yellowFlagLeftOrig)
        time.sleep(0.2)
        setYellowFlag(grey, grey, grey, yellowFlagLeftOrig)
        time.sleep(0.1)

def pulseGreen():
    global hit
    hit = False
    while (hit == False):
        setGreenFlag(green, green, green, greenFlagLeftOrig)
        time.sleep(0.2)
        setGreenFlag(grey, grey, grey, greenFlagLeftOrig)
        time.sleep(0.1)

def pulseBlue():
    global hit
    hit = False
    while (hit == False):
        setBlueFlag(blue, blue, blue, blueFlagLeftOrig)
        time.sleep(0.2)
        setBlueFlag(grey, grey, grey, blueFlagLeftOrig)
        time.sleep(0.1)
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
def setRedFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    
    pygame.draw.line(screen, colorLeft, (spaceList[0]-20,spaceList[1]), (spaceList[0]+39,spaceList[1]+39), 8)  # draw button
    
    pygame.draw.rect(screen, colorMiddle, (spaceList[0]+5,spaceList[1]-5,spaceList[2]-30,spaceList[3]+10))  # draw button
    
    pygame.draw.line(screen, colorRight, (spaceList[0]-20,spaceList[1]+39), (spaceList[0]+39,spaceList[1]), 8)  # draw button
    

def setOrangeFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    
    pygame.draw.line(screen, colorLeft, (spaceList[0]-20,spaceList[1]), (spaceList[0]+39,spaceList[1]+39), 8)  # draw button
    
    pygame.draw.rect(screen, colorMiddle, (spaceList[0]+5,spaceList[1]-5,spaceList[2]-30,spaceList[3]+10))  # draw button
    
    pygame.draw.line(screen, colorRight, (spaceList[0]-20,spaceList[1]+39), (spaceList[0]+39,spaceList[1]), 8)  # draw button
    

def setWhiteFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    
    pygame.draw.line(screen, colorLeft, (spaceList[0]-20,spaceList[1]), (spaceList[0]+39,spaceList[1]+39), 8)  # draw button
    
    pygame.draw.rect(screen, colorMiddle, (spaceList[0]+5,spaceList[1]-5,spaceList[2]-30,spaceList[3]+10))  # draw button
    
    pygame.draw.line(screen, colorRight, (spaceList[0]-20,spaceList[1]+39), (spaceList[0]+39,spaceList[1]), 8)  # draw button
    
    

def setYellowFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    
    pygame.draw.line(screen, colorLeft, (spaceList[0]-20,spaceList[1]), (spaceList[0]+39,spaceList[1]+39), 8)  # draw button
    
    pygame.draw.rect(screen, colorMiddle, (spaceList[0]+5,spaceList[1]-5,spaceList[2]-30,spaceList[3]+10))  # draw button
    
    pygame.draw.line(screen, colorRight, (spaceList[0]-20,spaceList[1]+39), (spaceList[0]+39,spaceList[1]), 8)  # draw button
    
def setGreenFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    
    pygame.draw.line(screen, colorLeft, (spaceList[0]-20,spaceList[1]), (spaceList[0]+39,spaceList[1]+39), 8)  # draw button
    
    pygame.draw.rect(screen, colorMiddle, (spaceList[0]+5,spaceList[1]-5,spaceList[2]-30,spaceList[3]+10))  # draw button
    
    pygame.draw.line(screen, colorRight, (spaceList[0]-20,spaceList[1]+39), (spaceList[0]+39,spaceList[1]), 8)  # draw button
    
def setBlueFlag(colorLeft, colorMiddle, colorRight, space):
    spaceList = list(space)
    
    pygame.draw.line(screen, colorLeft, (spaceList[0]-20,spaceList[1]), (spaceList[0]+39,spaceList[1]+39), 8)  # draw button
    
    pygame.draw.rect(screen, colorMiddle, (spaceList[0]+5,spaceList[1]-5,spaceList[2]-30,spaceList[3]+10))  # draw button
    
    pygame.draw.line(screen, colorRight, (spaceList[0]-20,spaceList[1]+39), (spaceList[0]+39,spaceList[1]), 8)  # draw button
    
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
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
    secNum = float(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = float(before[before.find(",", 9)+2:before.find(")")])
    returning = (firstNum, secNum, thirdNum)
    print("Returning:" + str(returning))
    return returning

def refresh():
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

def showTargets(rand, count, i):
    allInfo = pd.read_excel(path + "/flagCode/song" + str(rand[count]+1) + ".xlsx")
    screen.fill([0,0,0])
    #print(len(allInfo))
    #print(str(i)+ " "+ str(toColor(df.loc[(i),'Red 1'])))
    #print(toTuple(allInfo.loc[(i),'red Left']))
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'red Left']), (120, 330), (160, 370), 8)  # draw button
    pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'red Middle']), redButton)  # draw button
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'red Right']), (160, 330), (120, 370), 8)  # draw button
    
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'orange Left']), (400, 280), (440, 320), 8)  # draw button
    pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'orange Middle']), orangeButton)  # draw button
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'orange Right']), (440, 280), (400, 320), 8)  # draw button

    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'white Left']), (290, 190), (330, 230), 8)  # draw button
    pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'white Middle']), whiteButton)  # draw button
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'white Right']), (330, 190), (290, 230), 8)  # draw button

    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'yellow Left']), (150, 220), (190, 260), 8)  # draw button
    pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'yellow Middle']), yellowButton)  # draw button
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'yellow Right']), (190, 220), (150, 260), 8)  # draw button

    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'green Left']), (240, 160), (280, 200), 8)  # draw button
    pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'green Middle']), greenButton)  # draw button
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'green Right']), (280, 160), (240, 200), 8)  # draw button

    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'blue Left']), (420, 100), (460, 140), 8)  # draw button
    pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'blue Middle']), blueButton)  # draw button
    pygame.draw.line(screen, toTuple(allInfo.loc[(i),'blue Right']), (460, 100), (420, 140), 8)  # draw button


    
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