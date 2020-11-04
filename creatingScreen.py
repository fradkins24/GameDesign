# Sarah Fradkin
import pygame
#drawing Pygame
name=input("What is your name? ")
ask=input("Do you want to make a colorful screen? (yes/no) ")
while ask=="yes":
    w=input("What do you want the width of your screen to be? (maximun is 800) ")
    w=int(w)
    while w>800 or w<0:
        w=input("Please print a number between 0 and 800. ")
        w=int(w)
    l=input("What do you want the length of your screen to be? (maximum is 800) ")
    l=int(l)
    while l>800 or l<0:
        l=input("Please print a number between 0 and 800. ")
        l=int(l)
    pygame.init() #always first command
    color=input("\nWhat color do you want your screen to be?\nCHOICES:\n\nred\norange\nyellow\ngreen\nblue\nteal\npurple\npink\nmagenta\nbrown\nblack\nwhite\n\n")
    if not color=="red" and not color=="orange" and not color=="yellow" and not color=="green" and not color=="blue" and not color=="teal" and not color =="purple" and not color =="pink" and not color =="magenta" and not color=="brown" and not color=="black" and not color=="white":
        color=input("Please choose one of the following:\n\nred\norange\nyellow\ngreen\nblue\nteal\npurple\npink\nmagenta\nbrown\nblack\nwhite\n\n")
    #colors
    red=(255,0,0)
    orange=(233,132,30)
    yellow=(255,255,0)
    green=(52,233,52)
    blue=(0,0,255)
    teal=(0,255,255)
    purple=(154,0,255)
    pink=(252,122,255)
    magenta=(202,15,127)
    brown=(94,46,34)
    black=(0,0,0)
    white=(255,255,255)

    screen=pygame.display.set_mode((w,l)) #tuple
    pygame.display.set_caption(name+"\'s Screen") #title
    run =True
    while run:
        pygame.time.delay(100) #miliseconds
        screen.fill((teal))
        pygame.display.update() #also updates
        for i in pygame.event.get(): #picks up anything that happens on screen
            print(i)
            if i.type == pygame.QUIT: #leaves game
                run=False
                #ask=input("Do you want to make another colorful screen? (yes/no) ")
