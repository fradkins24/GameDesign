#Sarah Fradkin
import random #bring from library (software)
import time

name=input("What is your name?") #asks user to put in name
print("Good luck", name, end = '' "!") #prints good luck with name
print() #prints and enter
gameWords=["pyhton","java","PHP","javaScript","computer","geeks","keyboard","laptop","headphones","hardware","software"] #creates list
gameWords=["java"]
#use the choice method of my random function to pick a word
answer=input("Do you want to guess a word?") #asks user this question

while answer == "yes": #while answer is yes, do following
    word=random.choice(gameWords) #choose a random word from gameWords
    guesses="" #this is for the guessed characters after the input
    turns=len(word)+1 #number of turns/uesses (length of word +1)
    while turns>0: #while there are turns left
        for char in word: #for characters in the word
            if char in guesses: #if you guess a charcter in the word
                print(char,end=" ") #print the character/letter
            else: #if not
                print("_",end=" ") #then print a space (_)
        if word in guesses:
            turns=0
            print("Good job! The word was",word,"\nYOU WIN!\n")
        print()
        guess=input("Give me a letter:") #asks user for a letter
        print()
        guesses+=guess #re assigns guesses so that it includes letters already stated
        turns=turns-1 #one less turn
    # if word in guesses:
    #     print("No more tunrs left\nGAME OVER you loose!\n")
    # else:
    #     print("Good job! The word was",word,"\nYOU WIN!\n")
    answer=input("Do you want to play again?")

time.sleep(5) #seconds
