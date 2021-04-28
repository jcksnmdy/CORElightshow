
def targetGameSetup():
    global startOn, targetOn, soundOn, lightOn, hitEventOn, target
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 28)
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Target Game Setup")
    targetFlagText = font.render('Target: Red', True, red)
    switchFlagText = font.render('Rotate throught targets', True, white)
    soundEventText = font.render('What Sound on hit', True, white)
    lightEventText = font.render('Light Color on Hit', True, white)
    selectHitEventToggleText = font.render('Execute on hit', True, white)
    targetOnText = font.render('On', True, black)
    soundText = font.render('Pew', True, black)
    lightText = font.render('Flag Color', True, white)
    hitEventText = font.render('Off', True, white)
    startText = font.render('Start', True, black)
    playEffect = "pew"

    redFlag = pygame.Rect(300, 40, 39, 39)
    whiteFlag = pygame.Rect(350, 40, 39, 39)
    orangeFlag = pygame.Rect(400, 40, 39, 39)
    greenFlag = pygame.Rect(450, 40, 39, 39)
    blueFlag = pygame.Rect(500, 40, 39, 39)
    yellowFlag = pygame.Rect(550, 40, 39, 39)
    
    redFlagColorCenter = red
    orangeFlagColorCenter = orange
    whiteFlagColorCenter = white
    blueFlagColorCenter = blue
    yellowFlagColorCenter = yellow
    greenFlagColorCenter = green
    
    while True:
        
        screen.fill(black)
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                main()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                if redFlag.collidepoint(mouse_pos):
                    target = 1
                    targetFlagText = font.render('Target: Red', True, red)

                if whiteFlag.collidepoint(mouse_pos):
                    target = 3
                    targetFlagText = font.render('Target: White', True, white)
                
                if orangeFlag.collidepoint(mouse_pos):
                    target = 2
                    targetFlagText = font.render('Target: Orange', True, orange)
                
                if blueFlag.collidepoint(mouse_pos):
                    target = 6
                    targetFlagText = font.render('Target: Blue', True, blue)
                
                if greenFlag.collidepoint(mouse_pos):
                    target = 5
                    targetFlagText = font.render('Target: Green', True, green)
                
                if yellowFlag.collidepoint(mouse_pos):
                    target = 4
                    targetFlagText = font.render('Target: Yellow', True, yellow)

                if switchTargetToggle.collidepoint(mouse_pos):
                    if (targetOn == grey):
                        targetOn = white
                        targetOnText = font.render('On', True, black)
                    else:
                        targetOn = grey
                        targetOnText = font.render('Off', True, white)

                if selectSoundToggle.collidepoint(mouse_pos):
                    if (soundOn == grey):
                        soundOn = white
                        soundText = font.render('Pew', True, black)
                        playEffect = "pew"
                    elif (soundOn == white):
                        soundOn = red
                        soundText = font.render('ka-ching', True, black)
                        playEffect = "ka-ching"
                    else:
                        soundOn = grey
                        soundText = font.render('Off', True, black)
                        playEffect = "none"
                
                if selectLightToggle.collidepoint(mouse_pos):
                    if (lightOn == grey):
                        lightOn = (128,0,128)
                        lightText = font.render('Flag Color', True, black)
                    elif (lightOn == (128,0,128)):
                        lightOn = red
                        lightText = font.render('Red', True, white)
                    elif (lightOn == red):
                        lightOn = green
                        lightText = font.render('Green', True, white)
                    elif (lightOn == green):
                        lightOn = blue
                        lightText = font.render('Blue', True, white)
                    elif (lightOn == blue):
                        lightOn = (orange)
                        lightText = font.render('Orange', True, white)
                    elif (lightOn == (orange)):
                        lightOn = yellow
                        lightText = font.render('Yellow', True, white)
                    elif (lightOn == yellow):
                        lightOn = white
                        lightText = font.render('White', True, black)
                    else:
                        lightOn = grey
                        lightText = font.render('Off', True, white)

                if start.collidepoint(mouse_pos):
                    startTargetGame(2, playEffect, target)
                
        pygame.draw.rect(screen, redFlagColorCenter, (300, 40, 39, 39))  # draw button
        pygame.draw.rect(screen, whiteFlagColorCenter, (350, 40, 39, 39))  # draw button
        pygame.draw.rect(screen, orangeFlagColorCenter, (400, 40, 39, 39))  # draw button
        pygame.draw.rect(screen, greenFlagColorCenter, (450, 40, 39, 39))  # draw button
        pygame.draw.rect(screen, blueFlagColorCenter, (500, 40, 39, 39))  # draw button
        pygame.draw.rect(screen, yellowFlagColorCenter, (550, 40, 39, 39))  # draw button

        pygame.draw.rect(screen, startOn, start)  # draw button
        pygame.draw.rect(screen, targetOn, switchTargetToggle)  # draw button
        pygame.draw.rect(screen, soundOn, selectSoundToggle)  # draw button
        pygame.draw.rect(screen, lightOn, selectLightToggle)  # draw button
        pygame.draw.rect(screen, hitEventOn, selectHitEventToggle)  # draw button
        
        screen.blit(startText, start)
        screen.blit(targetFlagText, (29, 40))
        screen.blit(switchFlagText, (29, 110))
        screen.blit(soundEventText, (29, 180))
        screen.blit(lightEventText, (29, 260))
        screen.blit(selectHitEventToggleText, (29, 330))
        screen.blit(targetOnText, switchTargetToggle)
        screen.blit(soundText, selectSoundToggle)
        screen.blit(lightText, selectLightToggle)
        screen.blit(hitEventText, selectHitEventToggle)

        pygame.display.flip()
        
        clock.tick(60)

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
    global redFlagColorCenter, whiteFlagColorCenter, orangeFlagColorCenter, yellowFlagColorCenter, greenFlagColorCenter, blueFlagColorCenter, hit
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
    
    hit = False
    count = 0
    print(rand)
    print("Removing " + str(targetFlag))
    rand.remove(targetFlag-1)
    print(rand)
    while (count < 6):
        print("Target: " + str(targetFlag))
        setRedFlag(red, grey, grey, redFlagCenterOrig)
        setOrangeFlag(orange, grey, grey, orangeFlagCenterOrig)
        setWhiteFlag(white, grey, grey, whiteFlagCenterOrig)
        setYellowFlag(yellow, grey, grey, yellowFlagCenterOrig)
        setBlueFlag(blue, grey, grey, blueFlagCenterOrig)
        setGreenFlag(green, grey, grey, greenFlagCenterOrig)
        if (targetFlag == 1):
            setRedFlag(red, grey, red, redFlagCenterOrig)
            pygame.mixer.music.load("effects/targetRed.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseRed, name=None)
            pulse.start()
        elif (targetFlag == 2):
            setOrangeFlag(orange, grey, orange, orangeFlagCenterOrig)
            pygame.mixer.music.load("effects/targetOrange.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseOrange, name=None)
            pulse.start()
        elif (targetFlag == 3):
            setWhiteFlag(white, grey, white, whiteFlagCenterOrig)
            pygame.mixer.music.load("effects/targetWhite.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseWhite, name=None)
            pulse.start()
        elif (targetFlag == 4):
            setYellowFlag(yellow, grey, yellow, yellowFlagCenterOrig)
            pygame.mixer.music.load("effects/targetYellow.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseYellow, name=None)
            pulse.start()
        elif (targetFlag == 5):
            setGreenFlag(green, grey, green, greenFlagCenterOrig)
            pygame.mixer.music.load("effects/targetGreen.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseGreen, name=None)
            pulse.start()
        elif (targetFlag == 6):
            setBlueFlag(blue, grey, blue, blueFlagCenterOrig)
            pygame.mixer.music.load("effects/targetBlue.mp3")
            pygame.mixer.music.play(0)
            pulse = threading.Thread(group=None, target=pulseBlue, name=None)
            pulse.start()
        time.sleep(1)
        while (hit == False):
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
                            hit = True
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
                            setWhiteFlag(grey, grey, grey, whiteFlagCenterOrig)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informWhite.mp3")
                            pygame.mixer.music.play(0)
                            
                            time.sleep(2.5)
                            hit = True
                    
                    if orangeFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 2):
                            setOrangeFlag(grey, grey, grey, orangeFlagCenterOrig)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informOrange.mp3")
                            pygame.mixer.music.play(0)
                            
                            time.sleep(2.5)
                            hit = True

                    if yellowFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 4):
                            setYellowFlag(yellow, grey, yellow, yellowFlagCenterOrig)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informYellow.mp3")
                            pygame.mixer.music.play(0)

                            time.sleep(2.5)
                            hit = True
                    
                    
                    if greenFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 5):
                            setGreenFlag(green, grey, green, greenFlagCenterOrig)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informGreen.mp3")
                            pygame.mixer.music.play(0)
                            
                            time.sleep(2.5)
                            hit = True

                    if blueFlagOuter.collidepoint(mouse_pos):
                        if (targetFlag == 6):
                            setBlueFlag(blue, grey, blue, blueFlagCenterOrig)
                            pygame.mixer.music.load("effects/" + soundEffect + ".mp3")
                            pygame.mixer.music.play(0)
                            time.sleep(1.5)
                            pygame.mixer.music.load("effects/informBlue.mp3")
                            pygame.mixer.music.play(0)
                        
                            time.sleep(2.5)
                            hit = True
                    
                    

            screen.fill([0,0,0])

            pygame.draw.rect(screen, redFlagColorOuter, redFlagOuter)  # draw button
            pygame.draw.rect(screen, orangeFlagColorOuter, orangeFlagOuter)  # draw button
            pygame.draw.rect(screen, whiteFlagColorOuter, whiteFlagOuter)  # draw button
            pygame.draw.rect(screen, yellowFlagColorOuter, yellowFlagOuter)  # draw button
            pygame.draw.rect(screen, greenFlagColorOuter, greenFlagOuter)  # draw button
            pygame.draw.rect(screen, blueFlagColorOuter, blueFlagOuter)  # draw button

            pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
            pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
            pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
            pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
            pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
            pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button

            pygame.draw.rect(screen, redFlagColorCenter, redFlagCenter)  # draw button
            pygame.draw.rect(screen, orangeFlagColorCenter, orangeFlagCenter)  # draw button
            pygame.draw.rect(screen, whiteFlagColorCenter, whiteFlagCenter)  # draw button
            pygame.draw.rect(screen, yellowFlagColorCenter, yellowFlagCenter)  # draw button
            pygame.draw.rect(screen, greenFlagColorCenter, greenFlagCenter)  # draw button
            pygame.draw.rect(screen, blueFlagColorCenter, blueFlagCenter)  # draw button

            pygame.display.flip()   
            clock.tick(60)
        sparkle.join()
        pulse.join()
        targetFlag = ((rand[count-1])+1)
        print(rand)
        hit = False
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
