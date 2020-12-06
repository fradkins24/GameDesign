#Sarah Fradkin

#Pseudo code

#define variables
#make image lists and variables for randomizing them
#make scores files
#function for menu with three choices(easy, medium, hard, scores, exit) that go to where user pressed/chose
#function for scores screen (score=how many turns before wining)
#function that draws screen with cards that knows when not to show cards
#main function: tracks click, flips over to main side if no match, takes away cards it they do math, calculates turns/score, adds scores to file at the end, goes to menu when done
#run game
import pygame, time, random

#setup
WIDTH=800
HEIGHT=800
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Memory Game!")

#image lists
#easy
matches1=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg")]
random.shuffle(matches1)
define1={}
for number in range(12):
    define1["e{0}".format(number)]=matches1[number]

#medium
matches2=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\turtle.jpg")]
random.shuffle(matches2)
define2={}
for number in range(18):
    define2["m{0}".format(number)]=matches2[number]

#hard
matches3=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\zebra.jpg"),pygame.image.load("images\\zebra.jpg"),pygame.image.load("images\\bee.jpg"),pygame.image.load("images\\bee.jpg"),pygame.image.load("images\\ladybug.jpg"),pygame.image.load("images\\ladybug.jpg")]
random.shuffle(matches3)
define3={}
for number in range(24):
    define3["h{0}".format(number)]=matches3[number]

pics0=pygame.transform.scale(define1["e0"],(110,110))
pics1=pygame.transform.scale(define1["e1"],(110,110))
pics2=pygame.transform.scale(define1["e2"],(110,110))
screen.fill((0,0,0))
screen.blit(pics0,(0,5))
screen.blit(pics1,(0,110+10))
screen.blit(pics0,(0,110*2+15))
screen.blit(pics1,(0,110*3+20))
screen.blit(pics2,(0,110*4+25))
pygame.display.update()
pygame.time.delay(1000)
