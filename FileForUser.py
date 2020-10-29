#Sarah Fradkin
import os

def choices(): #choices menu
    print("* * * * * * * * * * * * * * * * * * * *")
    print("*               CHOICES               *")
    print("*                                     *")
    print("*    1) delete file                   *")
    print("*    2) add something to your file    *")
    print("*    3) write something in your file~ *")
    print("*    4) print what is in your file    *")
    print("*    5) close and stop editing file   *")
    print("*                                     *")
    print("* ~ WARNING: if you choose to write   *")
    print("* something in your file, all other   *")
    print("* will be lost!                       *")
    print("*                                     *")
    print("*       What do you want to do?       *")
    print("* * * * * * * * * * * * * * * * * * * *")

create=input("Do you want to create a file? (yes/no) ") #asks if user wants to create a file
while create=="yes": #if answer is yes
    #asks to put in name of file
    fileName=input("\nWhat do you want your file to be called? \nIf you want to edit an existing file, put that name in. ")
    #ass if they want to write anything and warns that everything will be esared if they do
    starting=input("\nDo you want to write something in you file? (yes/no) \n*if this is an old file and you write something, everything in it will be lost.*\n")
    if starting=="yes": #if user wants to write something, asks what
        thisFile=open(fileName, "w")
        content=input("What information do you want your file to have? ") #asks what user wants to be in file
        thisFile.write(content)
        thisFile.close() #closes file
    choices() #print choices
    answer=input() #asks for choice
    while answer =="1" or answer=="2" or answer=="3" or answer=="4" or answer=="5": #if the answer is not five
        if answer=="1": #if it's one delete file
            os.remove(fileName)
            break
        if answer=="2": #if two asks what user wants to add
            add=input("What do you want to add to your file? ")
            added=("\n"+add)
            thisFile=open(fileName, "a")
            thisFile.write(added)
            thisFile.close()
            break
        if answer=="3": #if three asks what user wants to write
            write=input("What do you want to write in your file? ")
            thisFile=open(fileName, "w")
            thisFile.write(write)
            thisFile.close()
            break
        if answer=="4": #if four prints what is in file
            thisFile=open(fileName, "r")
            print(thisFile.read())
            thisFile.close()
            break
        if answer=="5": #if the answer
            break
    #if answer not 1, 2, 3, 4, or 5 says to print one of them
    while not answer=="1" and not answer=="2" and not answer =="3" and not answer=="4" and not answer=="5":
        print("Please print a 1, 2, 3, 4, or 5. ")
        choices()
        answer=input()
    #asks if user wants to edit the file again or if they want to make another
    create=input("If you want to continue editing your file or create a new one, type \"yes\"\nOtherwise, type \"no\"\n")
