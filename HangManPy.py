# Maria Suarez
# Create a Hanggman version of the game:
# Use images in a list, Use Fonts, render them
import os, sys, time, pygame, random, math

os.system('cls')
pygame.init()

#Create my display screen
WIDTH = 800  # uppercase because it behaves as constant
HEIGHT = 500 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman GAME!")

# Define Colors
WHITE = [255,255,255]
BLACK = [0,0,0]

# Word lists
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']

# DEfine Font objects
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size 
WordFont=pygame.font.SysFont("comicsans", 50)
LetterFont=pygame.font.SysFont("comicsans",40)

# load images to list
images = []
for i in range(7):
    image=pygame.image.load("ImagesHM\\hangman"+ str(i)+".png")
    images.append(image)
    # screen.blit(images[i], (100,100))
    # pygame.display.update()
    # pygame.time.delay(300)

#Define Letters for rectangular buttons
Wbox = 30
dist = 10
letters = []
startx = round((WIDTH - (Wbox * 1.5 + dist) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + dist * 2 + ((Wbox * 1.5 + dist) * (i % 13))
    y = starty + ((i // 13) * (dist + Wbox * 2))
    letters.append([x, y, chr(A + i), True])

#Function to update screen
def updateScreen(turns,displayWord):
    screen.fill(WHITE)
    #Display Title
    title=TitleFont.render("Hangman",1, BLACK)
    centerTitle= WIDTH/2-title.get_width()/2
    screen.blit(title, (centerTitle,20))
    #Display Word
    textW=WordFont.render(displayWord,1, BLACK)
    screen.blit(textW, (300,150))
    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.rect(screen, BLACK, (x-Wbox/2, y-Wbox/2, Wbox,Wbox), width=1)
            text = LetterFont.render(ltr, 1, BLACK)
            screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    screen.blit(images[turns], (100, 100))
    pygame.display.update()
#End of game message 
def display_message(message):
    pygame.time.delay(1000)
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
#Update word function
def updateWord():  # function with a parameter to update word
    displayWord=""
    for char in word:
        if char in guesses:
            #print(char,end=' ')
            displayWord += char+" "
        else:
            displayWord += "_ "
            #print('_', end =' ')
   
    return displayWord

#always have a way to close your screen
check = True
FPS = 60
clock = pygame.time.Clock()
word=random.choice(gameWords).upper()
print(word)
turns= 0   #should we conider controlling this number when he/she misses
guesses=[]
while check:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    rect=pygame.Rect(x-Wbox/2, y-Wbox/2,Wbox,Wbox)
                    if rect.collidepoint(m_x,m_y):
                        letter[3] = False
                        guesses.append(ltr)
                        print(ltr)
                        if ltr not in word:
                            turns += 1
                            print(turns)
    displayWord=updateWord()
    updateScreen(turns, displayWord)
            #end of whole loop with 
    won = True
    for letter in word:
        if letter not in guesses:
            won = False
            break

    if won:
        display_message("You WON!")
        break

    if turns == 6:
        display_message("You LOST!")
        break
pygame.quit()
sys.exit()
