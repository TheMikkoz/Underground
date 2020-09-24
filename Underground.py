import pygame as pg

#Logger
def Debug(Value):
    with open("logs/debug.txt", 'w') as debugFile:
        debugFile.write(str(Value))

if __name__ == "__main__":
    #Initialise game engine
    pg.init()

    #Window settings
    win = pg.display.set_mode((200, 200))

    #Main loop active
    Run = True

    #Limit Frame per sec
    Clock = pg.time.Clock()

    #Loading assets
    def LoadAssets():
        Dictionary = {"1":pg.image.load("assets/01.png")}
        return Dictionary
    try:
        Asset = LoadAssets()
    except:
        Debug("Couldn't load assets.")

    #Drawing method
    def Draw():
        win.fill(0)
        win.blit(Asset["1"], (0,0))
        pg.display.flip()
        
    #Main loop
    while Run:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                Run = False
        Draw()
        Clock.tick(60)
    
    #Shutdown
    pg.quit()

else:
    Debug("!! -- !! -- !!")