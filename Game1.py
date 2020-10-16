#Sarah Fradkin
import random #bring from library (software)
import time

name=input("What is your name?")
print("Good luck", name, end = '' "!")
print()
gameWords=["pyhton","java","PHP","javaScript","computer","geeks","keyboard","laptop","headphones","hardware","software"]
#use the choice method of my random function to pick a word
answer=input("Do you want to guess a word?")

while answer == "yes": #while answer is yes, do following
    word=random.choice(gameWords)
    guesses=""
    turns=6
    while turns>0:
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_", end=" ")
        guess=input("Give me a letter:")
        guesses+=guess
        turns=turns-1

    print(word)
    answer=input("Do you want to play again?")

time.sleep(5) #seconds
