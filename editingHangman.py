#Sarah Fradkin

#what to fix:
#in the while run, I need to put that if the user wants to exit, run becoms false, and the window closes
#make menu
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
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# set up fonts
INFO_FONT = pygame.font.SysFont('comicsans', 20)
MENU_FONT = pygame.font.SysFont('comicsans', 30)
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
words = ["CHERRY","BERRY"] # make it longer
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

def menu():
    screen.fill(WHITE)
    a=70
    text = INFO_FONT.render("Once you choose your level, guess the letters you think", 1, BLACK)
    text2 = INFO_FONT.render("will be in your word. The letter will then disappear. If the", 1, BLACK)
    text3 = INFO_FONT.render("letter you pressed was in the word, it will appear in", 1, BLACK)
    text4 = INFO_FONT.render("place of one of the dashes. If the letter is not in", 1, BLACK)
    screen.blit(text, (20, a))
    screen.blit(text2, (20, a+5+text.get_height()))
    screen.blit(text3, (20, a+10+text.get_height()*2))
    screen.blit(text4, (20, a+15+text.get_height()*3))
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(10000)

def draw():
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
        if visible:
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    screen.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    screen.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        menu()
        #draw()

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

#while True:

main()
