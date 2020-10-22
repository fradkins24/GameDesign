#Sarah Fradkin
import random

numbers={"cero":0,"uno":1,"dos":2,"tres":3,"cuatro":4,"cinco":5,"seis":6,"siete":7,"ocho":8,"nueve":9,"diez":10}
verbs={"correr":"to run","escribir":"to write","dibujar":"to draw","cantar":"to sing","hablar":"to talk","nadar":"to swim","dormir":"to sleep"}

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
menu()
# def guess_verb():
#     h
#
#
# while type=="2":
#
