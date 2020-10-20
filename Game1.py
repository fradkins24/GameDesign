#Sarah Fradkin
import random #bring from library (software)
import time

name=input("What is your name? ") #asks user to put in name
gameWords=["strawberry","banana","papaya","mango","watermelon","melon","orange","cherry","raspberry","blackberry","grape","grapefruit","apple","peach","pear","nectarine"] #creates list
#use the choice method of my random function to pick a word
answer=input("Do you want to guess a fruit? (yes/no) ") #asks user this question

while answer == "yes": #while answer is yes, do following
    print() #prints and enter
    head=(" O") #defining body parts
    larm=(" O\n/")
    body=(" O\n/|")
    rarm=(" O\n/|\\")
    lleg=(" O\n/|\\\n/")
    rleg=(" O\n/|\\\n/ \\")
    word=random.choice(gameWords) #choose a random word from gameWords
    letters_left=len(word) #creates variable for letters left to guess
    guesses="" #this is for the guessed characters after the input
    turns=6 #6 turns bc 6 body parts
    print("You have",turns,"turns. Every time you guess wrong another body part will appear and a turn will be reduced.\nOnce the entire body is printed, you loose.\nGood luck", name, end = '' "!\n") #prints good luck with name and says number of turns
    while turns>0 and letters_left>0: #while there are turns left and letters to guess
        for char in word: #for characters in the word
            if char in guesses: #if you guess a charcter in the word
                print(char,end=" ") #print the character/letter
            else: #if not
                print("_",end=" ") #then print a space (_)
        print() #prints enter after pritning word or _
        guess=input("Give me a letter:") #asks user for a letter
        print() #prints enter to seperate each turn
        count=0 #makes count 0 each time loop repeats
        if guess[0] not in guesses: #if the guess isn't already in guesses
            count=word.count(guess[0]) #counts how many times guess appears in word
            if guess not in word: #if the guess is wrong
                turns=turns-1 #take away one turn
        if turns ==5: #for every amount of turns print a body part
            print(head)
        if turns==4:
            print(larm)
        if turns==3:
            print(body)
        if turns==2:
            print(rarm)
        if turns==1:
            print(lleg)
        if turns==0:
            print(rleg)
        letters_left=letters_left-count #sybtracts amount of count from letter left to guess
        guesses+=guess #re assigns guesses so that it includes letters already stated
    if letters_left==0: #after the loop end, if uou guessed all the letters
        print("Good job! The word was",word,end=''".\nYOU WIN!\n") #print that user won
    else: #if not
        print("You have 0 turns left.\nGAME OVER YOU LOOSE!\n") #print that they lost
    answer=input("Do you want to play again? (yes/no) ") #asks if user wants to play again and then restarts loop is "yes"

if not answer == "yes":
    print('Thank you for playing!')

time.sleep(1) #seconds
