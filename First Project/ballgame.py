import pygame
import msvcrt as m

#import tensorflow as tf
#tf.__version__

from random import randint
pygame.init()
pygame.font.init()

#font
myfont = pygame.font.SysFont('Comic Sans MS', 30)


#screen parameters
scwidth = 800
scheight = 800

win = pygame.display.set_mode((scwidth,scheight))

pygame.display.set_caption("BALLGAME")

#set ball to middle of the screen
x = 400		
#set ball above the bottom of the screen
y = scheight-50

#Quantities for the ball
velx = 0
width = 50
height = 50
radius = 10
accel = 1

y_rect=50;


start_ticks=pygame.time.get_ticks()


#rectangle class
class rectangle():

    def __init__(self,width,height,speed,x):
        self.width = width			#rectangle width
        self.height = height		#rectangle height
        self.x = x					#rectangle x coordinate
        self.y = self.height/2		#rectangle y coordinate
        self.send = False			#true if rectangle is showing
        self.speed = speed			#downwards velocity 





#Initialize rectangles array
rectangles = [rectangle(50,20,2,randint(0,scwidth)) for i in range(10)]

#Send a rectangle
def sendRectangle(ran):

    #Turn on rectangles randomly
    if (ran) == 1:
         rectangles[0].send = True
    elif ran == 2:
        rectangles[1].send = True
    elif ran == 3:
        rectangles[2].send = True
    elif ran == 4:
        rectangles[3].send = True
    elif ran == 5:
        rectangles[4].send = True
    elif ran == 6:
        rectangles[5].send = True
    elif ran == 7:
        rectangles[6].send = True


    #if rectangle i is alive
    for i in range(0,9):
        if rectangles[i].send == True:
			#draw rectangle i
            pygame.draw.rect(win, (0,0,255), (rectangles[i].x,rectangles[i].y,rectangles[i].width,rectangles[i].height),0)
            rectangles[i].y +=rectangles[i].speed
			#if rectangle reaches the bottom of the screen
            if rectangles[i].y >= (scheight-rectangles[i].height):
                rectangles[i].send=False 
                rectangles[i].y=0
                rectangles[i].x=randint(0,scwidth)


def collision():

    Surf = pygame.display.get_surface()
    
    if (x + radius) > 0 and (x + radius) < scwidth:

        #If any of the pixels around the ball are blue
        if (Surf.get_at((x + radius,scheight - 50)) == (0,0,255)):
            return True
        else:
            return False

    else:
        return False


run = True

#While game is running
while run:

    score = pygame.time.get_ticks()/100
    scoreSurface = myfont.render(str(score),False, (0,10,0))

	#set vel to 0 if and move to the edge of the screen if the ball reaches the edge of the screen
    if x>=scwidth-radius:
        x=scwidth-radius
        velx=0

    if x<=radius:
        x=radius
        velx=0

    #time delay
    pygame.time.delay(5)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            run = False

    if keys[pygame.K_LEFT]:		
        if velx>=0:
            velx=0
            velx-=accel
        if pygame.time.get_ticks()%5==0:
            velx-=accel

    if keys[pygame.K_RIGHT]:
        if velx<0:
            velx=0
            velx+=accel
        if pygame.time.get_ticks()%5==0:
            velx+=accel

    #move ball by velocity
    x+=velx

    #reset screen
    win.fill((50,50,50))

    #send a rectangle
    ran = randint(0,100)
    sendRectangle(ran)

    #If user collides with a rectangle
    if collision():

        textsurface = myfont.render("You died :( \n Press q to continue",False, (0,0,0))
        win.blit(textsurface,((scwidth/2)-10,(scheight/2)-10))

        pygame.draw.circle(win, (255,50,0), (x,y), radius)
        win.blit(scoreSurface,(0,0))

        pygame.display.update()

        #Stop updating the screen until the user presses q and then exit the game
        while run:
            #not sure why this needs to be initialized again
            pygame.init()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_q]:
                    run = False

    pygame.draw.circle(win, (255,50,0), (x,y), radius)
    win.blit(scoreSurface,(0,0))

    pygame.display.update()


pygame.display.quit()
pygame.quit()