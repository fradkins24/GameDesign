#Sarah Fradkin

#what to fix:
#in the while run, I need to put that if the user wants to exit, run becoms false, and the window closes
#make menu
#game code depends on what player chooses
#give user choice to play again
#window only closes if player closes it

import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# setup  button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
a=90
b=20
left=200
down=400
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

#open files for scores that start with 0
#easy file
file1= open("easyHMScores.txt", "w")
file1.write("0")
file1.close()
#medium file
file2=open("mediumHMScores.txt", "w")
file2.write("0")
file2.close()
#hard file
file3=open("hardHMScores.txt", "w")
file3.write("0")
file3.close()

# set up fonts
SCORES_FONT = pygame.font.SysFont('comicsansms', 50)
INFO_FONT = pygame.font.SysFont('comicsansms', 21)
MENU_FONT = pygame.font.SysFont('comicsans', 45)
CHOICE_FONT = pygame.font.SysFont('comicsans', 45)
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("images\hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words1 = ["CHERRY"]#,"BERRY","GRAPE","LIME","APPLE","BANANA","PEAR"] # make it longer
words2 = ["STRAWBERRY","ORANGE","MANGO","MELON","PAPAYA","LEMON","PINEAPPLE"]
words3= ["GRAPEFRUIT","CRANBERRY","RASPBERRY","POMEGRANATE","WATERMELON","CANTALOUPE"]
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (196, 224, 255)
GREEN = (74, 189, 41)
YELLOW = (231, 195, 0)
RED = (196, 52, 41)

def draw(i):
    word=random.choice(i)
    screen.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, 20)) # Notice centering

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    screen.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        #if visible:
        pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    screen.blit(images[hangman_status], (150, 100))
    pygame.display.update()

#display whether player won or lost
def display_message(message):
    pygame.time.delay(1000)
    screen.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#mains code for game
def main(i):
    FPS = 60
    clock = pygame.time.Clock()
    global hangman_status
    hangman_status=0
    # guessed = []
    word=random.choice(i)
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    for letter in letters:
                        x, y, ltr, visible = letter
                        #if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
            draw(i)

            won = True
            for letter in word:
                if letter not in guessed:
                    won = False
                    break

            if won:
                display_message("You WON!")
                break
            if hangman_status == 6:
                display_message("You LOST!")
                break
            #if easy setting
            if i==words1:
                score=str(6-hangman_status)
                file1 = open("easyHMScores.txt", "r")
                for line in file1:
                    #if line < score :
                    if str(line.split()) <score:
                        file1.close()
                        file1=open("easyHMScores.txt","w")
                        file1.write(score)
                        file1.close()
                file1.close()
            #if medium setting
            if i==words2:
                score=str((6-hangman_status)*2)
                file2 = open("mediumHMScores.txt", "r")
                for line in file2:
                    if str(line.split()) <score:
                        file2.close()
                        file2=open("mediumHMScores.txt","w")
                        file2.write(score)
                        file2.close()
                file2.close()
            #if hard setting
            if i==words3:
                score=str((6-hangman_status)*3)
                file3 = open("hardHMScores.txt", "r")
                for line in file3:
                    if str(line.split()) <score:
                        file3.close()
                        file3=open("hardHMScores.txt","w")
                        file3.write(score)
                file3.close()

    # word=random.choice(i)
    # clock.tick(FPS)
    # #checks what user pressed
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         run = False
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         m_x, m_y = pygame.mouse.get_pos()
    #         for letter in letters:
    #             x, y, ltr, visible = letter
    #             if visible:
    #                 dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
    #                 if dis < RADIUS:
    #                     letter[3] = False
    #                     guessed.append(ltr)
    #                     if ltr not in word:
    #                         hangman_status += 1
    # draw(i)
    #
    # won = True
    # for letter in word:
    #     if letter not in guessed:
    #         won = False
    #         break
    #
    # if won:
    #     display_message("You WON!")
    #     #break
    #
    # if hangman_status == 6:
    #     display_message("You LOST!")
    #     #break

def best_scores():
    screen.fill(BLUE)
    text = TITLE_FONT.render("BEST SCORES FOR:", 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    #easy scores
    file1=open("easyHMScores.txt","r")
    score=file1.read()
    easy = SCORES_FONT.render("Easy:  "+score,1,GREEN)
    file1.close()
    screen.blit(easy,(WIDTH/2 - easy.get_width()/2, 300))
    #mediu scores
    file2=open("mediumHMScores.txt","r")
    score2=file2.read()
    medium = SCORES_FONT.render("Medium:  "+score,1,YELLOW)
    file2.close()
    screen.blit(medium,(WIDTH/2 - medium.get_width()/2, 400))

    pygame.display.update()
best_scores()
#make menu with instructions and choice
def menu():

    screen.fill(BLUE)
    text = TITLE_FONT.render("LET'S PLAY HANGMAN!", 1, BLACK)
    screen.blit(text, (100, 20))#WIDTH/2 - text.get_width()

    #instructions
    text = INFO_FONT.render("Once you choose your level, guess the letters you think will be in your word.", 1, BLACK)
    text2 = INFO_FONT.render("The letter will then disappear. If the letter you pressed was in the word,", 1, BLACK)
    text3 = INFO_FONT.render("it will appear in place of one of the dashes. If the letter was not in the word,", 1, BLACK)
    text4 = INFO_FONT.render("then a body part will appear. If the entire body appears, you lose. If you guess", 1, BLACK)
    text5 = INFO_FONT.render("the entire word, you win. All the words are fruits. Good luck!",1,BLACK)
    screen.blit(text, (b, a))
    screen.blit(text2, (b, a+5+text.get_height()))
    screen.blit(text3, (b, a+10+text.get_height()*2))
    screen.blit(text4, (b, a+15+text.get_height()*3))
    screen.blit(text5, (b, a+20+text.get_height()*4))

    choice = CHOICE_FONT.render("CHOICES:",1,BLACK)
    screen.blit(choice,(b+50, a+70+text.get_height()*5))
    #3 circles
    pygame.draw.circle(screen, BLACK, (left, down), RADIUS, 3)
    pygame.draw.circle(screen, BLACK, (left, down+RADIUS*2+20), RADIUS, 3)
    pygame.draw.circle(screen, BLACK, (left, down+RADIUS*4+40), RADIUS, 3)
    pygame.draw.circle(screen, BLACK, (left, down+RADIUS*6+60), RADIUS, 3)

    #choice 1
    one=MENU_FONT.render("1",1,GREEN)
    screen.blit(one,(left-8,down-12))
    choice1=MENU_FONT.render("Easy",1,GREEN)
    screen.blit(choice1,(235,down-15))

    #choice2
    two=MENU_FONT.render("2",1,YELLOW)
    screen.blit(two,(left-8,down+RADIUS*2+6))
    choice2=MENU_FONT.render("Meduim",1,YELLOW)
    screen.blit(choice2,(235,down+45))

    #choice 3
    three=MENU_FONT.render("3",1,RED)
    screen.blit(three,(left-8,down+RADIUS*4+25))
    choice3=MENU_FONT.render("Hard",1,RED)
    screen.blit(choice3,(235,down+105))

    #choice 4
    four=MENU_FONT.render("4",1,BLACK)
    screen.blit(four,(left-8,down+RADIUS*6+45))
    choice4=MENU_FONT.render("EXIT",1,BLACK)
    screen.blit(choice4,(235,down+165))

    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         m_x, m_y = pygame.mouse.get_pos()
    #         dis = math.sqrt((left - m_x)**2 + (down - m_y)**2)
    #         if dis<RADIUS:
    #         #if left>m_x>left+RADIUS and down>m_y>down+RADIUS:
    #             main(words1)
    #         else:
    #             dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*2+20) - m_y)**2)
    #             if dis<RADIUS:
    #                 main(words2)
    #             else:
    #                 dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*4+40) - m_y)**2)
    #                 if dis<RADIUS:
    #                     main(words3)
    #                 else:
    #                     dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*6+60) - m_y)**2)
    #                     if dis<RADIUS:
    #                         run = False

    pygame.display.update()


FPS = 60
clock = pygame.time.Clock()
menu()
run=True
while run:
    guessed = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            dis = math.sqrt((left - m_x)**2 + (down - m_y)**2)
            if dis<RADIUS:
            #if left>m_x>left+RADIUS and down>m_y>down+RADIUS:
                main(words1)
            else:
                dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*2+20) - m_y)**2)
                if dis<RADIUS:
                    main(words2)
                else:
                    dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*4+40) - m_y)**2)
                    if dis<RADIUS:
                        main(words3)
                    else:
                        dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*6+60) - m_y)**2)
                        if dis<RADIUS:
                            run = False
            # elif m_x==left and m_y==down+RADIUS*2+20:
            #     main(words2)
            # elif m_x==left and m_y==down+RADIUS*4+40:
            #     main(words3)
            # elif m_x==left and m_y==down+RADIUS*6+60:
            #     run = False
            menu()
