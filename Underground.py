from os import environ
#Remove 'Hello from the pygame community. https://www.pygame.org/contribute.html' text from console
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg

#Logger
def Debug(Value):
    data = ""
    with open("logs/debug.txt") as debugFile:
        data = debugFile.read()
    with open("logs/debug.txt", 'w') as debugFile:
        debugFile.write(data + "\n" + str(Value))

if __name__ == "__main__":
    #Initialise game engine
    pg.init()

    #Window settings
    winX = 800
    winY = 800
    winSize = winX, winY
    #Position to middle
    environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0,0)
    environ['SDL_VIDEO_CENTERED'] = '0'
    win = pg.display.set_mode(winSize, pg.NOFRAME)

    #Main loop active
    Run = True

    #Limit Frame per sec
    Clock = pg.time.Clock()

    def image(png):
        img = pg.image.load("assets/img/" + png)
        return img

    #Loading assets
    def LoadAssets():
        Dictionary = {
            "1":image("background/01.png"),
            "exit0":image("exit/exitX00.png"),
            "exit1":image("exit/exitX01.png"),
            "player":{
                    "headIdle":{
                        0:image("player/headIdle00.png"),
                        1:image("player/headIdle01.png"),
                        2:image("player/headIdle02.png"),
                        3:image("player/headIdle00.png"),
                        4:image("player/headIdle00.png"),
                    },
                    #"":image(".png"),
                    #"":image(".png"),
                    "tail":image("player/tail00.png"),
                    "tailEnd":image("player/tailEnd00.png"),
                    }       
            }
        return Dictionary
    try:
        Asset = LoadAssets()
    except Exception as exp:
        Debug("Couldn't load assets. " + str(exp))

    #user events
    usereventDic = {"playerAnimation":pg.USEREVENT # 24
    }
    eventTimerDic = {"playerAnimation": 200}
    for dic in usereventDic:
        pg.time.set_timer(usereventDic[dic], eventTimerDic[dic])

    #Hover
    exitHover = False

    #>| Background |<
    posX = 0
    posY = 0
    def backgroundCheck(var):
        if var == "both":
            if posX <= 32:
                posX += 1
            else: 
                posX = 0
            if posY <= 32:
                posY += 1
            else: 
                posY = 0
        elif var == "y":
            if posY <= 32:
                posY += 1
            else: 
                posY = 0
        elif var == "x":
            if posX <= 32:
                posX += 1
            else: 
                posX = 0
        else:
            if posX <= 32:
                pass
            else: 
                posX = 0
            if posY <= 32:
                pass
            else: 
                posY = 0

    #Drawing method
    def Draw():
        #Background
        for i in range(int(winX / 32 + 2)):
            for ii in range(int(winY / 32 + 2)):
                win.blit(Asset["1"], ((-32 + posX + 32 * i),(-32 + posY + 32 * ii)))
        
        if exitHover == True:
            win.blit(Asset["exit1"], (winX - 32 ,0))
        else:
            win.blit(Asset["exit0"], (winX - 32 ,0))

        #Update display
        pg.display.update()
        
    #Main loop
    while Run:
        #Mouse position
        mousePos = pg.mouse.get_pos()
        #Mouse button
        mouseButton = pg.mouse.get_pressed()

        #Event handler
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                Run = False
            if mousePos[0] > winX - 30 and mousePos[0] < winX and mousePos[1] > 0 and mousePos[1] < 30:
                exitHover = True
                if mouseButton[0] != 0:
                    Run = False
            else:
                exitHover = False
            
            
        Draw()
        Clock.tick(60)
    
    #Shutdown
    pg.quit()

else:
    Debug("!! -- !! -- !!")