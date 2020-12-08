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
import pygame, time, random, math

WIDTH=800
HEIGHT=800
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Memory Game!")

#variables
size=100
margin=size+12
RADIUS = 20
infoy=90
infox=20
left=200
down=400
x=12
y=12

#defining back of card
square1=pygame.image.load("images\\backofCard.jpg")
square1=pygame.transform.scale(square1,(size,size))
square2=pygame.image.load("images\\backofCard.jpg")
square2=pygame.transform.scale(square2,(size,size))
square3=pygame.image.load("images\\backofCard.jpg")
square3=pygame.transform.scale(square3,(size,size))
square4=pygame.image.load("images\\backofCard.jpg")
square4=pygame.transform.scale(square4,(size,size))


square5=pygame.image.load("images\\backofCard.jpg")
square5=pygame.transform.scale(square5,(size,size))
square6=pygame.image.load("images\\backofCard.jpg")
square6=pygame.transform.scale(square6,(size,size))
square7=pygame.image.load("images\\backofCard.jpg")
square7=pygame.transform.scale(square7,(size,size))
square8=pygame.image.load("images\\backofCard.jpg")
square8=pygame.transform.scale(square8,(size,size))


square9=pygame.image.load("images\\backofCard.jpg")
square9=pygame.transform.scale(square9,(size,size))
square10=pygame.image.load("images\\backofCard.jpg")
square10=pygame.transform.scale(square10,(size,size))
square11=pygame.image.load("images\\backofCard.jpg")
square11=pygame.transform.scale(square11,(size,size))
square12=pygame.image.load("images\\backofCard.jpg")
square12=pygame.transform.scale(square12,(size,size))


square13=pygame.image.load("images\\backofCard.jpg")
square13=pygame.transform.scale(square13,(size,size))
square14=pygame.image.load("images\\backofCard.jpg")
square14=pygame.transform.scale(square14,(size,size))
square15=pygame.image.load("images\\backofCard.jpg")
square15=pygame.transform.scale(square15,(size,size))
square16=pygame.image.load("images\\backofCard.jpg")
square16=pygame.transform.scale(square16,(size,size))


square17=pygame.image.load("images\\backofCard.jpg")
square17=pygame.transform.scale(square17,(size,size))
square18=pygame.image.load("images\\backofCard.jpg")
square18=pygame.transform.scale(square18,(size,size))
square19=pygame.image.load("images\\backofCard.jpg")
square19=pygame.transform.scale(square19,(size,size))
square20=pygame.image.load("images\\backofCard.jpg")
square20=pygame.transform.scale(square20,(size,size))

square21=pygame.image.load("images\\backofCard.jpg")
square21=pygame.transform.scale(square21,(size,size))
square22=pygame.image.load("images\\backofCard.jpg")
square22=pygame.transform.scale(square22,(size,size))
square23=pygame.image.load("images\\backofCard.jpg")
square23=pygame.transform.scale(square23,(size,size))
square24=pygame.image.load("images\\backofCard.jpg")
square24=pygame.transform.scale(square24,(size,size))

square25=pygame.image.load("images\\backofCard.jpg")
square25=pygame.transform.scale(square25,(size,size))
square26=pygame.image.load("images\\backofCard.jpg")
square26=pygame.transform.scale(square26,(size,size))
square27=pygame.image.load("images\\backofCard.jpg")
square27=pygame.transform.scale(square27,(size,size))
square28=pygame.image.load("images\\backofCard.jpg")
square28=pygame.transform.scale(square28,(size,size))


#colors
white=(255,255,255)
black=(0,0,0)
blue = (196, 224, 255)
green = (74, 189, 41)
yellow = (231, 195, 0)
red = (196, 52, 41)
purple = (158, 98, 170)

#fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 60)
INFO_FONT = pygame.font.SysFont('comicsansms', 21)
STAR_FONT = pygame.font.SysFont('comicsansms', 18)
MENU_FONT = pygame.font.SysFont('comicsans', 45)
CHOICE_FONT = pygame.font.SysFont('comicsans', 45)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


#image lists
#easy
matches1=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg")]
random.shuffle(matches1)
define1={}
for number in range(12):
    define1["b{0}".format(number)]=matches1[number]

#medium
matches2=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\zebra.jpg"),pygame.image.load("images\\zebra.jpg")]
random.shuffle(matches2)
define2={}
for number in range(20):
    define2["b{0}".format(number)]=matches2[number]

#hard
matches3=[pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\panda.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\bat.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\elephant.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\giraffe.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\hippo.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\lion.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\monkey.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\snake.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\turtle.jpg"),pygame.image.load("images\\zebra.jpg"),pygame.image.load("images\\zebra.jpg"),pygame.image.load("images\\bee.jpg"),pygame.image.load("images\\bee.jpg"),pygame.image.load("images\\ladybug.jpg"),pygame.image.load("images\\ladybug.jpg"),pygame.image.load("images\\crab.jpg"),pygame.image.load("images\\crab.jpg"),pygame.image.load("images\\starfish.jpg"),pygame.image.load("images\\starfish.jpg"),]
random.shuffle(matches3)
define3={}
for number in range(28):
    define3["b{0}".format(number)]=matches3[number]

# pics0=pygame.transform.scale(define1["e0"],(110,110))
# pics1=pygame.transform.scale(define1["e1"],(110,110))
# pics2=pygame.transform.scale(define1["e2"],(110,110))
# screen.fill((0,0,0))
# screen.blit(pics0,(0,5))
# screen.blit(pics1,(0,110+10))
# screen.blit(pics0,(0,110*2+15))
# screen.blit(pics1,(0,110*3+20))
# screen.blit(pics2,(0,110*4+25))

#draw screen/grid
def draw(dict):
    global score, square1, square2, square3, square4, square5, square6, square7, square8, square9, square10, square11, square12, square13, square14, square15, square16, square17, square18, square19, square20, square21, square22, square23, square24, square25, square26, square27, square28
    global up1, up2, up3, up4, up5, up6, up7, up8, up9, up10, up11, up12, up13, up14, up15, up16, up17, up18, up19, up20, up21, up22, up23, up24, up25, up26, up27, up28
    screen.fill(black)
    # up9=True
    #for hard

    # screen.blit(square1,(x,y))
    # screen.blit(square2,(x+margin,y))
    # screen.blit(square3,(x+margin*2,y))
    # screen.blit(square4,(x+margin*3,y))

    # screen.blit(square5,(x,y+margin))
    # screen.blit(square6,(x+margin,y+margin))
    # screen.blit(square7,(x+margin*2,y+margin))
    # screen.blit(square8,(x+margin*3,y+margin))

    if up9==True:
        screen.blit(square9,(x,y+margin*2))
    else:
        pic0=pygame.transform.scale(dict["b0"],(size,size))
        screen.blit(pic0,(x,y+margin*2))
    if up10==True:
        screen.blit(square10,(x+margin,y+margin*2))
    else:
        pic1=pygame.transform.scale(dict["b1"],(size,size))
        screen.blit(pic1,(x+margin,y+margin*2))
    if up11==True:
        screen.blit(square11,(x+margin*2,y+margin*2))
    else:
        pic2=pygame.transform.scale(dict["b2"],(size,size))
        screen.blit(pic2,(x+margin*2,y+margin*2))
    if up12==True:
        screen.blit(square12,(x+margin*3,y+margin*2))
    else:
        pic3=pygame.transform.scale(dict["b3"],(size,size))
        screen.blit(pic3,(x+margin*3,y+margin*2))

    screen.blit(square13,(x,y+margin*3))
    screen.blit(square14,(x+margin,y+margin*3))
    screen.blit(square15,(x+margin*2,y+margin*3))
    screen.blit(square16,(x+margin*3,y+margin*3))

    screen.blit(square17,(x,y+margin*4))
    screen.blit(square18,(x+margin,y+margin*4))
    screen.blit(square19,(x+margin*2,y+margin*4))
    screen.blit(square20,(x+margin*3,y+margin*4))

    # for column in range(0,400,size+margin):
    #     column=int(column)
    #     for row in range(0,300,size+margin):
    #         row=int(row)
    #         square1=pygame.image.load("images\\backofCard.jpg")
    #         square=pygame.transform.scale(square1,(size,size))
    #         screen.blit(square,(column+20,row+239))
            #square=pygame.draw.rect(screen,(white),(column+20,row+239,size,size))
    text=SCORE_FONT.render("Score: "+score,1,white)
    screen.blit(text,(550,380))
    pygame.display.update()

#main code
def main(dict):
    global score, square1, square2, square3, square4, square5, square6, square7, square8, square9, square10, square11, square12, square13, square14, square15, square16, square17, square18, square19, square20, square21, square22, square23, square24, square25, square26, square27, square28
    global up1, up2, up3, up4, up5, up6, up7, up8, up9, up10, up11, up12, up13, up14, up15, up16, up17, up18, up19, up20, up21, up22, up23, up24, up25, up26, up27, up28
    up1=True
    up2=True
    up3=True
    up4=True
    up5=True
    up6=True
    up7=True
    up8=True
    up9=True
    up10=True
    up11=True
    up12=True
    up13=True
    up14=True
    up15=True
    up16=True
    up17=True
    up18=True
    up19=True
    up20=True
    up21=True
    up22=True
    up23=True
    up24=True
    up25=True
    up26=True
    up27=True
    up28=True

    score=str(0)
    run=True
    # draw()
    count=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() and count<2:
                    pos=pygame.mouse.get_pos()
                    pos=pos[0]//(size+x),pos[1]//(size+y)
                    if pos[0]==0 and pos[1]==2:
                        # pic0=pygame.transform.scale(dict["b0"],(size,size))
                        # screen.blit(pic0,(x,y+margin*2))
                        #up9=False
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                        up9=False
                    if pos[0]==1 and pos[1]==2:
                        # pic1=pygame.transform.scale(dict["b1"],(size,size))
                        # screen.blit(pic1,(x+margin,y+margin*2))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                        up10=False
                    if pos[0]==2 and pos[1]==2:
                        # pic2=pygame.transform.scale(dict["b2"],(size,size))
                        # screen.blit(pic2,(x+margin*2,y+margin*2))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                        up11=False
                    if pos[0]==3 and pos[1]==2:
                        # pic3=pygame.transform.scale(dict["b3"],(size,size))
                        # screen.blit(pic3,(x+margin*3,y+margin*2))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                        up12=False

                    if pos[0]==0 and pos[1]==3:
                        pic4=pygame.transform.scale(dict["b4"],(size,size))
                        screen.blit(pic4,(x,y+margin*3))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                    if pos[0]==1 and pos[1]==3:
                        pic5=pygame.transform.scale(dict["b5"],(size,size))
                        screen.blit(pic5,(x+margin,y+margin*3))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                    if pos[0]==2 and pos[1]==3:
                        pic6=pygame.transform.scale(dict["b6"],(size,size))
                        screen.blit(pic6,(x+margin*2,y+margin*3))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                    if pos[0]==3 and pos[1]==3:
                        pic7=pygame.transform.scale(dict["b7"],(size,size))
                        screen.blit(pic7,(x+margin*3,y+margin*3))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1

                    if pos[0]==0 and pos[1]==4:
                        pic8=pygame.transform.scale(dict["b8"],(size,size))
                        screen.blit(pic8,(x,y+margin*4))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                    if pos[0]==1 and pos[1]==4:
                        pic9=pygame.transform.scale(dict["b9"],(size,size))
                        screen.blit(pic9,(x+margin,y+margin*4))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                    if pos[0]==2 and pos[1]==4:
                        pic10=pygame.transform.scale(dict["b10"],(size,size))
                        screen.blit(pic10,(x+margin*2,y+margin*4))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                    if pos[0]==3 and pos[1]==4:
                        pic11=pygame.transform.scale(dict["b11"],(size,size))
                        screen.blit(pic11,(x+margin*3,y+margin*4))
                        # pygame.display.update()
                        # pygame.time.delay(1000)
                        count+=1
                    pygame.display.update()
        draw(dict)
                    # pygame.display.update()
#menu
def menu():
    runMenu=True
    while runMenu:
        screen.fill(blue)
        text = TITLE_FONT.render("LET'S PLAY A MEMORY GAME!", 1, black)
        screen.blit(text, (40, 20))

        #instructions
        text = INFO_FONT.render("Once you choose your level, that number of cards will appear face down. You", 1, black)
        text2 = INFO_FONT.render("will click on two cards at a time, and those cards will flip over showing an image.", 1, black)
        text3 = INFO_FONT.render("If the two images match, they will disappear. If they do not, they will flip back", 1, black)
        text4 = INFO_FONT.render("over and you will choose two more. This cycle will continue until all the cards", 1, black)
        text5 = INFO_FONT.render("are gone. Good luck!",1,black)
        screen.blit(text, (infox, infoy))
        screen.blit(text2, (infox, infoy+5+text.get_height()))
        screen.blit(text3, (infox, infoy+10+text.get_height()*2))
        screen.blit(text4, (infox, infoy+15+text.get_height()*3))
        screen.blit(text5, (infox, infoy+20+text.get_height()*4))

        choice = CHOICE_FONT.render("CHOICES:",1,black)
        screen.blit(choice,(infox+50, infoy+70+text.get_height()*5))
        #3 circles
        pygame.draw.circle(screen, black, (left, down), RADIUS, 3)
        pygame.draw.circle(screen, black, (left, down+RADIUS*2+20), RADIUS, 3)
        pygame.draw.circle(screen, black, (left, down+RADIUS*4+40), RADIUS, 3)
        pygame.draw.circle(screen, black, (left, down+RADIUS*6+60), RADIUS, 3)
        pygame.draw.circle(screen, black, (left, down+RADIUS*8+80), RADIUS, 3)

        #choice 1
        one=MENU_FONT.render("1",1,green)
        screen.blit(one,(left-8,down-12))
        choice1=MENU_FONT.render("Easy (12)",1,green)
        screen.blit(choice1,(235,down-15))

        #choice2
        two=MENU_FONT.render("2",1,yellow)
        screen.blit(two,(left-8,down+RADIUS*2+6))
        choice2=MENU_FONT.render("Meduim (20)",1,yellow)
        screen.blit(choice2,(235,down+45))

        #choice 3
        three=MENU_FONT.render("3",1,red)
        screen.blit(three,(left-8,down+RADIUS*4+25))
        choice3=MENU_FONT.render("Hard (28)",1,red)
        screen.blit(choice3,(235,down+105))

        #choice 4
        four=MENU_FONT.render("4",1,purple)
        screen.blit(four,(left-8,down+RADIUS*6+45))
        choice4=MENU_FONT.render("Best Scores*",1,purple)
        screen.blit(choice4,(235,down+165))

        #choice 5
        five=MENU_FONT.render("5",1,black)
        screen.blit(five,(left-8,down+RADIUS*8+65))
        choice5=MENU_FONT.render("EXIT",1,black)
        screen.blit(choice5,(235,down+225))

        #how to calculate scores
        star=STAR_FONT.render("*Your score is the number of turns it takes you to guess all the matches, so the lower the", 1, purple)
        star2=STAR_FONT.render("score the better.*",1,purple)
        screen.blit(star,(20,700))
        screen.blit(star2,(20,star.get_height()+705))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runMenu=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                dis = math.sqrt((left - m_x)**2 + (down - m_y)**2)
                if dis<RADIUS:
                    runMenu=False
                else:
                    dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*2+20) - m_y)**2)
                    if dis<RADIUS:
                        runMenu=False
                    else:
                        dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*4+40) - m_y)**2)
                        if dis<RADIUS:
                            runMenu=False
                        else:
                            dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*6+60) - m_y)**2)
                            if dis<RADIUS:
                                runMenu=False
                            else:
                                dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*8+80) - m_y)**2)
                                if dis<RADIUS:
                                    runMenu=False


        pygame.display.update()
main(define1)
