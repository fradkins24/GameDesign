# Sarah Fradkin
import pygame
pygame.init()

run=True
WIDTH=730
HIEGHT=475
x=300
y=400
speed=1
# walkR=[pygame.image.load("Sprites\kneeR.jpg")]#,pygame.image.load("Sprites\leapR.jnp")]
# walkL=[pygame.image.load("Sprites\kneeL.jpg"),pygame.image.load("Sprites\leapL.jpg")]
# stand=[pygame.image.load("Sprites\stand.jpg")]
screen=pygame.display.set_mode((WIDTH,HIEGHT)) #tuple
background=pygame.image.load("francepic.png")

pygame.display.set_caption("Testing Characters") #title
pygame.display.update()

def redrawWindow():
    screen.blit(background,(0,0))
    pygame.display.update()
# while run:
#     screen.blit(stand,(x,y))
#     for i in pygame.event.get(): #picks up anything that happens on screen
#         if i.type == pygame.QUIT: #leaves game
#             run=False
#
#     pressed=pygame.key.get_pressed()
#
#     if pressed[pygame.K_RIGHT] and x>0:
#         pygame.blit(walkR,(x,y))
#         x-=speed
#     if pressed[pygame.K_LEFT] and x<WIDTH:
#         screen.blit(walkL,(x,y))
#         x+=speed
    redrawWindow()
