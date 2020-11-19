# Sarah Fradkin
import pygame, time
pygame.init()
#defining variables
place=0
moveR=15
moveL=15
run=True
WIDTH=600
HIEGHT=700
x=300
y=550
speed=10
t=90
jump=False
high=10
clock=pygame.time.Clock()
#defining characters
forw=pygame.image.load("images\leapR.jpg")
walkR=[pygame.image.load("images\kneeR.jpg"),pygame.image.load("images\leapR.jpg")]
walkL=[pygame.image.load("images\kneeL.jpg"),pygame.image.load("images\leapL.jpg")]
stand=pygame.image.load("images\stand.jpg")
screen=pygame.display.set_mode((WIDTH,HIEGHT)) #tuple
background=pygame.image.load("images\\longForest.jpg")

wb=background.get_width()
w=forw.get_width() #width of charcater
wx=w+x

pygame.display.set_caption("Testing Characters") #title
pygame.display.update()
#control left and right
left=False
right=False
#control list
walkcount=0
# screen.blit(background,(place,0))
# pygame.display.update()
def redrawWindow(): #function for re-setting background and character
    global walkcount #makes sure it's using walkcount we created

    screen.blit(background,(place,0))
    pygame.display.update()
    screen.blit(stand,(x,y))
    pygame.display.update()
    if walkcount+1>=6:
        walkcount=0

    if left: #three pixels per pic then change
        screen.blit(walkL[walkcount//3], (x,y))
        walkcount+=1
        # screen.blit(background,(5,0))
        # pygame.display.update()
    elif right:
        screen.blit(walkR[walkcount//3], (x,y))
        walkcount+=1
        # screen.blit(background,(-5,0))
        # pygame.display.update()
    else:
        screen.blit(stand, (x,y))
        walkcount=0
    pygame.display.update()
while run:
    clock.tick(15)
    for i in pygame.event.get(): #picks up anything that happens on screen
        if i.type == pygame.QUIT: #leaves game
            run=False

    pressed=pygame.key.get_pressed()
    #moving left and right
    if pressed[pygame.K_RIGHT] and abs(place-wx)<wb:
        #x+=speed
        left=False
        right=True
        place-=moveR
        screen.blit(background,(place,0))
        pygame.display.update()
    elif pressed[pygame.K_LEFT] and abs(place-x)>0:
        #x-=speed
        left=True
        right=False
        place+=moveL
        screen.blit(background,(place,0))
        pygame.display.update()
    else:
        left=False
        right=False
        walkcount=0
    if not(jump): #jumpimg
        if pressed[pygame.K_SPACE]:
            jump=True
            left=False
            right=False
            walkcount=0
    elif high>=-10:
        y-=(high*abs(high))/2
        high-=1
    else:
        high=10
        jump=False
    redrawWindow() #calling function
