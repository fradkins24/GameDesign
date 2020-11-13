# Sarah Fradkin
import pygame
pygame.init()

run=True
WIDTH=730
HIEGHT=475
x=300
y=400
walkR=[pygame.image.load("Sprites\kneR.jpg"),pygame.image.load("Sprites\leapR.jnp")]
walkL=[pygame.image.load("Sprites\kneeL.jpg"),pygame.image.load("Sprites\leapL.jpg")]
stand=[pygame.image.load("Sprites\stand.jpg")]
screen=pygame.display.set_mode((WIDTH,HIEGHT)) #tuple
background=pygame.image.load("francepic.png")

pygame.display.set_caption("Testing Characters") #title
pygame.display.update()

def redrawWindow():
    screen.blit(background,(0.0))
    pygame.display.update()
