# Sarah Fradkin
import pygame, time
pygame.init()
#defining variables
run=True
WIDTH=730
HIEGHT=475
x=300
y=400
speed=50
t=90
jump=False
high=10
#defining characters
walkR=pygame.image.load("Sprites\kneeR.jpg")
walkR2=pygame.image.load("Sprites\leapR.jpg")
walkL=pygame.image.load("Sprites\kneeL.jpg")
walkL2=pygame.image.load("Sprites\leapL.jpg")
stand=pygame.image.load("Sprites\stand.jpg")
screen=pygame.display.set_mode((WIDTH,HIEGHT)) #tuple
background=pygame.image.load("francepic.png")

w=walkR.get_width() #width of charcater

pygame.display.set_caption("Testing Characters") #title
pygame.display.update()

def redrawWindow(): #function for re-setting background and character
    screen.blit(background,(0,0))
    pygame.display.update()
    screen.blit(stand,(x,y))
    pygame.display.update()
while run:
    # screen.blit(stand,(x,y))
    # pygame.display.update()
    for i in pygame.event.get(): #picks up anything that happens on screen
        if i.type == pygame.QUIT: #leaves game
            run=False

    pressed=pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT]:
        screen.blit(walkR,(x,y))
        pygame.display.update()
        pygame.time.delay(t) #pause to see both chacraters(running)
        screen.blit(walkR2,(x,y))
        pygame.display.update()
        pygame.time.delay(t)
        if x+w<WIDTH:
            x+=speed
    if pressed[pygame.K_LEFT]:
        screen.blit(walkL,(x,y))
        pygame.display.update()
        pygame.time.delay(t) #pause to see both chacraters(running)
        screen.blit(walkL2,(x,y))
        pygame.display.update()
        pygame.time.delay(t)
        if x>0:
            x-=speed
    if not(jump): #jumpimg
        if pressed[pygame.K_SPACE]:
            jump=True
    elif high>=-10:
        y-=(high*abs(high))/2
        high-=1
    else:
        high=10
        jump=False
#BECAUSE OF DELAY ON RUNNING, JUMPIMG IS VERY SLOW
#ASK HOW TO FIX IT
    redrawWindow() #calling function
