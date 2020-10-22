#Sarah Fradkin
import random

numbers={"cero":0, "uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5, "seis":6, "siete":7, "ocho":8, "nueve":9, "diez":10}
verbs={"correr":"to run","escribir":"to write","dibujar":"to draw","cantar":"to sing","hablar":"to talk","nadar":"to swim","dormir":"to sleep"}
# word1=random.choice(list(verbs))
# print(verbs[word1])

def menu():
    space=(" ")
    star=("* ")
    print(star*25)
    print(star,space*10,"Guessing Spanish Words",space*10,star,"\n*",space*45,"*")
    print("*    Instructions: Once you choose what type of *\n* word you want to guess, a word in Spanish will*\n* be printed and you will have to write its     *\n* meaning in English. Each time you play, you   *\n* will have three words to define.",space*12,"*")
    print("*",space*45,"*\n*",space*45,"*")
    print("*",space*18,"CHOICES",space*18,"*")
    print("* If you want to play:", space*24,"*\n*",space*2,"print the number (1) to guess a number",space*3,"*\n*",space*19,"OR",space*22,"*\n*",space*3,"print the number (2) to guess a verb",space*4,"*")
    print("*",space*45,"*")
    print("* If you DO NOT want to play:",space*17,"*\n*",space*2, "print the number (3)",space*21,"*")
    print(star*25)
    print()
    answer=input()

def main_code1():
    word1=random.choice(list(numbers))
    turn1=2
    guesses1=""
    print("What number is",word1,end='' "? ")
    while turn1>0 and str(numbers[word1]) not in str(guesses1):
        guess1=input()
        guesses1+=guess1
        turn1=turn1-1
        if str(numbers[word1]) not in str(guesses1):
            print("Try again.")
    if str(numbers[word1]) in str(guess1):
        turn1=0
        print("\nGood job!",word1,"means",numbers[word1],end='' "!\n")
    else:
        print("\nYou ran out of turns.",word1,"means",numbers[word1],end='' ". Better luck next time!\n")

def guess_number():
    print("When the word is printed, type in the number that coresponds to the word. You have two guesses per word.")
    main_code1()
    main_code1()
    main_code1()

def main_code2():
    word2=random.choice(list(verbs))
    turn2=3
    guesses2=""
    print("What does",word2,"mean? ")
    while turn2>0 and str(verbs[word2]) not in str(guesses2):
        guess2=input()
        guesses2+=guess2
        turn2=turn2-1
        if str(verb[word2]) not in str(guesses2):
            print("Try again.")
    if str(verb[word2]) in str(guess2):
        turn2=0
        print("\nGood job!",word2,"means",verb[word2],end='' "!\n")
    else:
        print("\nYou ran out of turns.",word2,"means",verb[word2],end='' ". Better luck next time!\n")

def guess_verb():
    print("When the word is printed, write the definition of the word in English. You have three guesses per word.")
    main_code2()
    main_code2()
    main_code2()

# while type=="2":
#
menu()
guess_number()
