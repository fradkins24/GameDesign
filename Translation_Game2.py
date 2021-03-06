#Sarah Fradkin
import random
import time

numbers={"cero":0, "uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5, "seis":6, "siete":7, "ocho":8, "nueve":9, "diez":10,"once":11,"doce":12,"trece":13,"catorce":14,"quince":15}
verbs={"Correr":"run","Escribir":"write","Dibujar":"draw","Cantar":"sing","Hablar":"talk","Nadar":"swim","Dormir":"sleep","Trabajar":"work","Leer":"read","Descansar":"rest","Comer":"eat","Patinar":"skate","Beber":"drink"}

def choices(): #function for telling/asking choices
    space=(" ")
    star=("* ")
    print("*",space*18,"CHOICES",space*18,"*")
    print("*",space*45,"*")
    print("*",space*5,"1) Guess a number", space*21,"*\n*",space*5,"2) Guess a verb",space*23,"*\n*",space*5,"3) Exit game",space*26,"*") #choices
    print(star*25)
    print()

def menu(): #instructions function
    space=(" ")
    star=("* ")
    print(star*25) #top border
    print(star,space*10,"Guessing Spanish Words",space*10,star,"\n*",space*45,"*") #title
    print("*    Instructions: Once you choose what type of *\n* word you want to guess, a word in Spanish will*\n* be printed and you will have to write its     *\n* meaning in English. Each time you play, you   *\n* will be presented with three words to",space*7,"*\n* translate.",space*34,"*") #game instructions
    print("*",space*45,"*")
    choices()

def main_code1():#main working code for numbers
    word1=random.choice(list(numbers)) #chooses random key in numbers
    turn1=2 #two turns
    #len1=len(str(numbers[word1])) #finds legnth of number (how many digits)
    guesses1="" #blank variable for while loop
    print("What number is",word1,end='' "? ") #asks what word means
    while turn1>0 and not str(guesses1) ==str(numbers[word1]): #while there are more than 0 turns and answer isn't guesses
        guess1=input() #input
        guesses1=guess1 #makes guesses=to guess to they can compare it to answer
        turn1=turn1-1 #subtracts turn1
        if not str(guesses1) ==str(numbers[word1]) and turn1>0: #if user guesses are wrong with turns left, it will print try again
            print("\nTry again.")
            print("What number is",word1,end='' "? ") #asks what word means again
    if str(guesses1) ==str(numbers[word1]): #if when the loop ends, the word is the guesses
        print("\nGood job! \""+word1.capitalize()+ "\" means",numbers[word1],end='' "!\n\n") #prints word and that they won
    else: #if word not in guesses
        print("\nYou ran out of turns. \""+word1.capitalize()+"\" means",numbers[word1],end='' ". Better luck next time!\n\n") #will print that they ran out of turns and tell them what word means

def guess_number(): #entire game code for numbers
    print("When the word is printed, type in the meaning of the word as a number. You have two guesses per word.") #specific instructions for numbers and how many turns
    main_code1() #prints main code three times so that three words are guessed
    main_code1()
    main_code1()

def main_code2(): #main code for verbs, same reasoning a numbers, only difference is number of turns
    word2=random.choice(list(verbs))
    turn2=3
    guesses2=""
    print(word2,"means: to ",end='')
    while turn2>0 and not str(verbs[word2])== str(guesses2):
        guess2=input()
        guesses2=guess2
        turn2=turn2-1
        if not str(verbs[word2])== str(guesses2) and turn2>0:
            print("\nTry again.")
            print(word2,"means: to ",end='')
    if str(verbs[word2]) == str(guess2):
        print("\nGood job! \""+word2+"\" means to",verbs[word2],end='' "!\n\n")
    else:
        print("\nYou ran out of turns. \""+word2+"\" means to",verbs[word2],end='' ". Better luck next time!\n\n")

def guess_verb(): #entire game codefor verbs, slightly different specific instructions
    print("When the word is printed, write the definition of the word in English. You have three guesses per word.")
    main_code2()
    main_code2()
    main_code2()

#GAME
menu() #prints entire menu, including instructions
answer=input() #asks for answer
while not answer=="3": #while the answer is anything but a three...
    if answer=="1": #if answer is one
        guess_number() #print numbers game code
    if answer=="2": #if answer is 2
        guess_verb() #prints verbs code
    if not answer =="1" and not answer=="2": # if answer isn't 1 or 2
        print("Please type in a 1, 2, or 3.\n") #asks to type a 1 2 or 3
    star=("* ")
    print(star*25,"")
    choices() #then prints only choices and aks for input
    answer=input()
if answer=="3": #if the answer is three
    print("Thank you for playing!") #printe thank you for playing and exits game

time.sleep(1) #sleeps one second
