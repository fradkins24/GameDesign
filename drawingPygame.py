#Sarah Fradkin
import pygame, time, sys
pygame.init()
#background pic has to be size of screen
background=pygame.image.load("francepic.png")
WIDTH=730
HIEGHT=475
screen=pygame.display.set_mode((WIDTH,HIEGHT)) #tuple
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
#screen.fill(white)
pygame.display.set_caption("My Shapes") #title
pygame.display.update()

run =True
x=20
y=20
w=50
h=100
r=50
jump=False
high=10
def redrawWindow():
    #screen.blit(picname,(x,y))
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,(10,123,10),(x,y, w,h))
    pygame.display.update()
    #                 window     color        x, y   radius thickness
    #pygame.draw.circle(screen,(100,100,255),(x+100,y+100),r,4)
    pygame.display.update()
while run:
    for i in pygame.event.get(): #picks up anything that happens on screen
        if i.type == pygame.QUIT: #leaves game
            run=False
    #                window    color      x,y(start)    w, h
    #we are going to move out rectangle around
    keyboardKey=pygame.key.get_pressed()
    #check what key was pressed
    speed=1
    if keyboardKey[pygame.K_LEFT] and x>0: #subtract from x
        x-=speed
        r-=speed
    if keyboardKey[pygame.K_RIGHT] and x+w<WIDTH: #add to x
        x+=speed
        r+=speed
    if not(jump): #this is for moving y without jump
        if keyboardKey[pygame.K_UP] and y>0: #subtract from y
            y-=speed
        if keyboardKey[pygame.K_DOWN] and y+h<HIEGHT: #add to y
            y+=speed
        if keyboardKey[pygame.K_SPACE]:
            jump=True
    else:
        if high>=-10:
            y-=(high*abs(high))/2
            high-=1
        else:
            high=10
            jump=False
    if keyboardKey[pygame.K_a] and w>5:
        w-=speed
    if keyboardKey[pygame.K_d] and x+w<WIDTH:
        w+=speed
    if keyboardKey[pygame.K_w] and h>5:
        h-=speed
    if keyboardKey[pygame.K_s] and y+h<HIEGHT:
        h+=speed
    redrawWindow()
