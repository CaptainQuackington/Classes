import pygame
pygame.init


### class definition--------------------------------------------
class clover:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        #stem
        pygame.draw.rect(screen, (0,150,85), (self.xpos-10, self.ypos+20, 15, 50))
        #leaves
        pygame.draw.circle(screen, (0,151,0), (self.xpos-20, self.ypos+20), 20) 
        pygame.draw.circle(screen, (85,150,0), (self.xpos, self.ypos-10), 20) 
        pygame.draw.circle(screen, (85,150,255), (self.xpos+20, self.ypos+20), 20) 
        #add one more leaf here!
class eggy:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        #stem
        pygame.draw.ellipse(screen, (255, 255, 0), (self.xpos, self.ypos, 50, 70))
        
        #add one more leaf here!


# end of class definition-----------------------------------------

#stamp (aka instantiate) clovers
clover1 = clover(200, 200)
clover2 = clover(400, 400)
clover3 = clover(100, 400)
clover4 = clover(400, 100)
clover5 = clover(300, 200)

eggy1 = eggy(100, 700)
eggy2 = eggy(600, 550)
eggy3 = eggy(400, 650)
#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("clover class demo")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed


#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
 

    #draw class objects
    clover1.draw()
    clover2.draw()
    clover3.draw()
    clover4.draw()
    clover5.draw()

    eggy1.draw()
    eggy2.draw()
    eggy3.draw()
    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()