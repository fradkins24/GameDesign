#Sarah Fradkin
import random #bring from library (software)
import time
from datetime import date

today = date.today()
date=str(today.strftime("%B %d, %Y"))

name=input("What is your name? ") #asks user to put in name
wordsFile=open("WordsGame1P2.txt","w")
wordsFile.write("strawberry\nbanana\npapaya\nmango\nwatermelon\nmelon\norange\ncherry\nraspberry\nblackberry\ngrape\ngrapefruit\napple\npeach\npear\nnectarine\npineapple\nblueberry\npomegranate\ncranberry\nlemon\nlime\ncoconut")
wordsFile.close()
wordsFile=open("WordsGame1P2.txt","r")
gameWords=wordsFile.read().splitlines()
wordsFile.close()
#gameWords=["strawberry","banana","papaya","mango","watermelon","melon","orange","cherry","raspberry","blackberry","grape","grapefruit","apple","peach","pear","nectarine"] #creates list
#use the choice method of my random function to pick a word
answer=input("Do you want to guess a fruit? (yes/no) ") #asks user this questio

while answer == "yes": #while answer is yes, do following
    score=0
    print("\nYou will guess five words and have 6 turns per word.\nEvery time you guess wrong another body part will appear and a turn will be reduced.\nOnce the entire body is printed, you loose. For every word you guess right, you will get one point.\nGood luck", name, end = '' "!\n") #prints good luck with name and says number of turns
    for i in range(5):
        print() #prints and enter
        head=(" O") #defining body parts
        larm=(" O\n/|")
        body=(" O\n |")
        rarm=(" O\n/|\\")
        lleg=(" O\n/|\\\n/")
        rleg=(" O\n/|\\\n/ \\")
        wordsFile=open("WordsGame1P2.txt","r")
        word=random.choice(gameWords) #choose a random word from gameWords
        letters_left=len(word) #creates variable for letters left to guess
        guesses="" #this is for the guessed characters after the input
        turns=6 #6 turns bc 6 body parts
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
                if guess[0] not in word: #if the guess is wrong
                    turns=turns-1 #take away one turn
            if turns ==5: #for every amount of turns print a body part
                print(head)
            if turns==4:
                print(body)
            if turns==3:
                print(larm)
            if turns==2:
                print(rarm)
            if turns==1:
                print(lleg)
            if turns==0:
                print(rleg)
            letters_left=letters_left-count #sybtracts amount of count from letter left to guess
            guesses+=guess[0] #re assigns guesses so that it includes letters already stated
        if letters_left==0: #after the loop end, if uou guessed all the letters
            score+=1
            print("Good job! The word was",word,end=''".\n") #print that user won
        else: #if not
            print("You have 0 turns left.\n") #print that they lost
    score=str(score)
    scoresFile=open("ScoresGame1P2.txt","a")
    scoresFile.write(name)
    scoresFile.write("    ")
    scoresFile.write(score)
    scoresFile.write("    ")
    scoresFile.write(date)
    scoresFile.write("\n")
    scoresFile.close()
    print("You got "+score+"/5 words correct. Here are other people's scores who have played.\n\n")
    scoresFile=open("ScoresGame1P2.txt","r")
    print(scoresFile.read())
    scoresFile.close()
    answer=input("\n\nDo you want to play again? (yes/no) ") #asks if user wants to play again and then restarts loop is "yes"

if not answer == "yes":
    print('Thank you for playing!')

time.sleep(1) #seconds
