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
square=pygame.image.load("images\\backofCard.jpg")
square=pygame.transform.scale(square,(size,size))


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

#defining images
panda=pygame.image.load("images\\panda.jpg")
bat=pygame.image.load("images\\bat.jpg")
elephant=pygame.image.load("images\\elephant.jpg")
giraffe=pygame.image.load("images\\giraffe.jpg")
hippo=pygame.image.load("images\\hippo.jpg")
lion=pygame.image.load("images\\lion.jpg")
monkey=pygame.image.load("images\\monkey.jpg")
snake=monkey,pygame.image.load("images\\snake.jpg")
turtle=pygame.image.load("images\\turtle.jpg")
zebra=pygame.image.load("images\\zebra.jpg")
bee=pygame.image.load("images\\bee.jpg")
ladybug=pygame.image.load("images\\ladybug.jpg")
crab=pygame.image.load("images\\crab.jpg")
starfish=pygame.image.load("images\\starfish.jpg")

#image lists
#easy
matches1=[panda,panda,bat,bat,elephant,elephant,giraffe,giraffe,hippo,hippo,lion,lion]
random.shuffle(matches1)
define1={}
for number in range(12):
    define1["b{0}".format(number)]=matches1[number]

#medium
matches2=[panda,panda,bat,bat,elephant,elephant,giraffe,giraffe,hippo,hippo,lion,lion,monkey,monkey,snake,snake,turtle,turtle,zebra,zebra]
random.shuffle(matches2)
define2={}
for number in range(20):
    define2["b{0}".format(number)]=matches2[number]

#hard
matches3=[panda,panda,bat,bat,elephant,elephant,giraffe,giraffe,hippo,hippo,lion,lion,monkey,monkey,snake,snake,turtle,turtle,zebra,zebra,bee,bee,ladybug,ladybug,crab,crab,starfish,starfish]
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
    global score, card_statis, square
    screen.fill(black)
    #cards to print based on difficulty

    if dict==define3:
        if card_statis[0][0]==0:
            screen.blit(square,(x,y))
        else:
            pic20=pygame.transform.scale(dict["b20"],(size,size))
            screen.blit(pic20,(x,y))
        if card_statis[0][1]==0:
            screen.blit(square,(x+margin,y))
        else:
            pic21=pygame.transform.scale(dict["b21"],(size,size))
            screen.blit(pic21,(x+margin,y))
        if card_statis[0][2]==0:
            screen.blit(square,(x+margin*2,y))
        else:
            pic22=pygame.transform.scale(dict["b22"],(size,size))
            screen.blit(pic22,(x+margin*2,y))
        if card_statis[0][3]==0:
            screen.blit(square,(x+margin*3,y))
        else:
            pic23=pygame.transform.scale(dict["b23"],(size,size))
            screen.blit(pic23,(x+margin*3,y))

        if card_statis[6][0]==0:
            screen.blit(square,(x,y+margin*6))
        else:
            pic24=pygame.transform.scale(dict["b24"],(size,size))
            screen.blit(pic23,(x,y+margin*6))
        if card_statis[6][1]==0:
            screen.blit(square,(x+margin,y+margin*6))
        else:
            pic25=pygame.transform.scale(dict["b25"],(size,size))
            screen.blit(pic25,(x+margin,y+margin*6))
        if card_statis[6][2]==0:
            screen.blit(square,(x+margin*2,y+margin*6))
        else:
            pic26=pygame.transform.scale(dict["b26"],(size,size))
            screen.blit(pic26,(x+margin*2,y+margin*6))
        if card_statis[6][3]==0:
            screen.blit(square,(x+margin*3,y+margin*6))
        else:
            pic27=pygame.transform.scale(dict["b27"],(size,size))
            screen.blit(pic27,(x+margin*3,y+margin*6))

    if dict==define2 or dict==define3:
        if card_statis[1][0]==0:
            screen.blit(square,(x,y+margin))
        else:
            pic12=pygame.transform.scale(dict["b12"],(size,size))
            screen.blit(pic12,(x,y+margin))
        if card_statis[1][1]==0:
            screen.blit(square,(x+margin,y+margin))
        else:
            pic13=pygame.transform.scale(dict["b13"],(size,size))
            screen.blit(pic13,(x+margin,y+margin))
        if card_statis[1][2]==0:
            screen.blit(square,(x+margin*2,y+margin))
        else:
            pic14=pygame.transform.scale(dict["b14"],(size,size))
            screen.blit(pic14,(x+margin*2,y+margin))
        if card_statis[1][3]==0:
            screen.blit(square,(x+margin*3,y+margin))
        else:
            pic15=pygame.transform.scale(dict["b15"],(size,size))
            screen.blit(pic15,(x+margin*3,y+margin))

        if card_statis[5][0]==0:
            screen.blit(square,(x,y+margin*5))
        else:
            pic16=pygame.transform.scale(dict["b16"],(size,size))
            screen.blit(pic16,(x,y+margin*5))
        if card_statis[5][1]==0:
            screen.blit(square,(x+margin,y+margin*5))
        else:
            pic17=pygame.transform.scale(dict["b17"],(size,size))
            screen.blit(pic17,(x+margin,y+margin*5))
        if card_statis[5][2]==0:
            screen.blit(square,(x+margin*2,y+margin*5))
        else:
            pic18=pygame.transform.scale(dict["b18"],(size,size))
            screen.blit(pic18,(x+margin*2,y+margin*5))
        if card_statis[5][3]==0:
            screen.blit(square,(x+margin*3,y+margin*5))
        else:
            pic19=pygame.transform.scale(dict["b19"],(size,size))
            screen.blit(pic19,(x+margin*3,y+margin*5))

    if card_statis[2][0]==0:
        screen.blit(square,(x,y+margin*2))
    else:
        pic0=pygame.transform.scale(dict["b0"],(size,size))
        screen.blit(pic0,(x,y+margin*2))
    if card_statis[2][1]==0:
        screen.blit(square,(x+margin,y+margin*2))
    else:
        pic1=pygame.transform.scale(dict["b1"],(size,size))
        screen.blit(pic1,(x+margin,y+margin*2))
    if card_statis[2][2]==0:
        screen.blit(square,(x+margin*2,y+margin*2))
    else:
        pic2=pygame.transform.scale(dict["b2"],(size,size))
        screen.blit(pic2,(x+margin*2,y+margin*2))
    if card_statis[2][3]==0:
        screen.blit(square,(x+margin*3,y+margin*2))
    else:
        pic3=pygame.transform.scale(dict["b3"],(size,size))
        screen.blit(pic3,(x+margin*3,y+margin*2))

    if card_statis[3][0]==0:
        screen.blit(square,(x,y+margin*3))
    else:
        pic4=pygame.transform.scale(dict["b4"],(size,size))
        screen.blit(pic4,(x,y+margin*3))
    if card_statis[3][1]==0:
        screen.blit(square,(x+margin,y+margin*3))
    else:
        pic5=pygame.transform.scale(dict["b5"],(size,size))
        screen.blit(pic5,(x+margin,y+margin*3))
    if card_statis[3][2]==0:
        screen.blit(square,(x+margin*2,y+margin*3))
    else:
        pic6=pygame.transform.scale(dict["b6"],(size,size))
        screen.blit(pic6,(x+margin*2,y+margin*3))
    if card_statis[3][3]==0:
        screen.blit(square,(x+margin*3,y+margin*3))
    else:
        pic7=pygame.transform.scale(dict["b7"],(size,size))
        screen.blit(pic7,(x+margin*3,y+margin*3))

    if card_statis[4][0]==0:
        screen.blit(square,(x,y+margin*4))
    else:
        pic8=pygame.transform.scale(dict["b8"],(size,size))
        screen.blit(pic8,(x,y+margin*4))
    if card_statis[4][1]==0:
        screen.blit(square,(x+margin,y+margin*4))
    else:
        pic9=pygame.transform.scale(dict["b9"],(size,size))
        screen.blit(pic9,(x+margin,y+margin*4))
    if card_statis[4][2]==0:
        screen.blit(square,(x+margin*2,y+margin*4))
    else:
        pic10=pygame.transform.scale(dict["b10"],(size,size))
        screen.blit(pic10,(x+margin*2,y+margin*4))
    if card_statis[4][3]==0:
        screen.blit(square,(x+margin*3,y+margin*4))
    else:
        pic11=pygame.transform.scale(dict["b11"],(size,size))
        screen.blit(pic11,(x+margin*3,y+margin*4))

    text=SCORE_FONT.render("Score: "+str(score),1,white)
    screen.blit(text,(550,380))
    pygame.display.update()

#main code
def main(dict):
    global score, card_statis, square
    clicked=[]
    tracking=[]
    card_statis=[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    score=0
    run=True
    draw(dict)
    count=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() and count<2:
                    pos=pygame.mouse.get_pos()
                    pos=pos[0]//(size+x),pos[1]//(size+y)

                    if dict==define2 or dict==define3:
                        if pos[0]==0 and pos[1]==1:
                            clicked.append(dict["b11"])
                            count+=1
                            card_statis[1][0]=1
                            tracking.append(1)
                            tracking.append(0)
                        if pos[0]==1 and pos[1]==1:
                            clicked.append(dict["b12"])
                            count+=1
                            card_statis[1][1]=1
                            tracking.append(1)
                            tracking.append(1)
                        if pos[0]==2 and pos[1]==1:
                            clicked.append(dict["b13"])
                            count+=1
                            card_statis[1][2]=1
                            tracking.append(1)
                            tracking.append(2)
                        if pos[0]==3 and pos[1]==1:
                            clicked.append(dict["b14"])
                            count+=1
                            card_statis[1][3]=1
                            tracking.append(1)
                            tracking.append(3)

                        if pos[0]==0 and pos[1]==6:
                            clicked.append(dict["b15"])
                            count+=1
                            card_statis[6][0]=1
                            tracking.append(6)
                            tracking.append(0)
                        if pos[0]==1 and pos[1]==6:
                            clicked.append(dict["b16"])
                            count+=1
                            card_statis[6][1]=1
                            tracking.append(6)
                            tracking.append(1)
                        if pos[0]==2 and pos[1]==6:
                            clicked.append(dict["b17"])
                            count+=1
                            card_statis[6][2]=1
                            tracking.append(6)
                            tracking.append(2)
                        if pos[0]==3 and pos[1]==6:
                            clicked.append(dict["b18"])
                            count+=1
                            card_statis[6][3]=1
                            tracking.append(6)
                            tracking.append(3)


                    if pos[0]==0 and pos[1]==2:
                        clicked.append(dict["b0"])
                        count+=1
                        card_statis[2][0]=1
                        tracking.append(2)
                        tracking.append(0)
                    if pos[0]==1 and pos[1]==2:
                        clicked.append(dict["b1"])
                        count+=1
                        card_statis[2][1]=1
                        tracking.append(2)
                        tracking.append(1)
                    if pos[0]==2 and pos[1]==2:
                        clicked.append(dict["b2"])
                        count+=1
                        card_statis[2][2]=1
                        tracking.append(2)
                        tracking.append(2)
                    if pos[0]==3 and pos[1]==2:
                        clicked.append(dict["b3"])
                        count+=1
                        card_statis[2][3]=1
                        tracking.append(2)
                        tracking.append(3)

                    if pos[0]==0 and pos[1]==3:
                        clicked.append(dict["b4"])
                        count+=1
                        card_statis[3][0]=1
                        tracking.append(3)
                        tracking.append(0)
                    if pos[0]==1 and pos[1]==3:
                        clicked.append(dict["b5"])
                        count+=1
                        card_statis[3][1]=1
                        tracking.append(3)
                        tracking.append(1)
                    if pos[0]==2 and pos[1]==3:
                        clicked.append(dict["b6"])
                        count+=1
                        card_statis[3][2]=1
                        tracking.append(3)
                        tracking.append(2)
                    if pos[0]==3 and pos[1]==3:
                        clicked.append(dict["b7"])
                        count+=1
                        card_statis[3][3]=1
                        tracking.append(3)
                        tracking.append(3)
                    if pos[0]==0 and pos[1]==4:
                        clicked.append(dict["b8"])
                        count+=1
                        card_statis[4][0]=1
                        tracking.append(4)
                        tracking.append(0)
                    if pos[0]==1 and pos[1]==4:
                        clicked.append(dict["b9"])
                        count+=1
                        card_statis[4][1]=1
                        tracking.append(4)
                        tracking.append(1)
                    if pos[0]==2 and pos[1]==4:
                        clicked.append(dict["b10"])
                        count+=1
                        card_statis[4][2]=1
                        tracking.append(4)
                        tracking.append(2)
                    if pos[0]==3 and pos[1]==4:
                        clicked.append(dict["b11"])
                        count+=1
                        card_statis[4][3]=1
                        tracking.append(4)
                        tracking.append(3)
                    draw(dict)

                    if count==2:
                        score+=1
                        if clicked[0]==clicked[1]:
                            print("yes")
                            clicked=[]
                            count=0
                            tracking=[]
                        else:
                            print("no")
                            clicked=[]
                            count=0
                            pygame.time.delay(800)
                            track1=tracking[0]
                            track2=tracking[1]
                            track3=tracking[2]
                            track4=tracking[3]
                            card_statis[track1][track2]=0
                            card_statis[track3][track4]=0
                            tracking=[]


                    draw(dict)
                    pygame.display.update()
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
        text3 = INFO_FONT.render("If the two images match, they will stay face up. If they do not, they will flip", 1, black)
        text4 = INFO_FONT.render("back over and you will choose two more. This cycle will continue until all the", 1, black)
        text5 = INFO_FONT.render("cards are face up. Good luck!",1,black)
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
main(define2)
