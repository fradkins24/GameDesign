# Sarah Fradkin
import pygame
#drawing pygame
#ask user for color
#ask size of window
#print color
pygame.init() #always first command
screen=pygame.display.set_mode((800,600)) #tuple
screen.fill((0,0,0)) #you select the color of background 0-255
pygame.display.flip() #updates
pygame.display.set_caption("Testing Pygame") #title
run =True
while run:
    pygame.time.delay(100) #miliseconds
    screen.fill((169,32,69))
    pygame.display.update() #also updates
    for eve in pygame.event.get(): #picks up anything that happens on screen
        print(eve)
        if eve.type == pygame.QUIT: #leaves game
            run=False
pygame.time.delay(50)
