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
e0=matches1[0]
e1=matches1[1]
e2=matches1[2]
e3=matches1[3]
e4=matches1[4]
e5=matches1[5]
e6=matches1[6]
e7=matches1[7]
e8=matches1[8]
e9=matches1[9]
e10=matches1[10]
e11=matches1[11]
#medium
matches2=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\turtle.jpg")]
random.shuffle(matches2)
m0=matches2[0]
m1=matches2[1]
m2=matches2[2]
m3=matches2[3]
m4=matches2[4]
m5=matches2[5]
m6=matches2[6]
m7=matches2[7]
m8=matches2[8]
m9=matches2[9]
m10=matches2[10]
m11=matches2[11]
m12=matches2[12]
m13=matches2[13]
m14=matches2[14]
m15=matches2[15]
m16=matches2[16]
m17=matches2[17]
#hard
matches3=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\zebra.jpg"),pygame.image.load("images\\zebra.jpg"),pygame.image.load("images\\bee.jpg"),pygame.image.load("images\\bee.jpg"),pygame.image.load("images\\ladybug.jpg"),pygame.image.load("images\\ladybug.jpg")]
random.shuffle(matches3)
h0=matches3[0]
h1=matches3[1]
h2=matches3[2]
h3=matches3[3]
h4=matches3[4]
h5=matches3[5]
h6=matches3[6]
h7=matches3[7]
h8=matches3[8]
h9=matches3[9]
h10=matches3[10]
h11=matches3[11]
h12=matches3[12]
h13=matches3[13]
h14=matches3[14]
h15=matches3[15]
h16=matches3[16]
h17=matches3[17]
h18=matches3[18]
h19=matches3[19]
h20=matches3[20]
h21=matches3[21]
h22=matches3[22]
h23=matches3[23]

pics0=pygame.transform.scale(e0,(110,110))
pics1=pygame.transform.scale(e1,(110,110))
pics2=pygame.transform.scale(e2,(110,110))
screen.fill((0,0,0))
screen.blit(pics0,(0,5))
screen.blit(pics1,(0,110+10))
screen.blit(pics0,(0,110*2+15))
screen.blit(pics1,(0,110*3+20))
screen.blit(pics2,(0,110*4+25))
pygame.display.update()
pygame.time.delay(1000)
