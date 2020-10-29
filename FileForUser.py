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

def main(): #main code
    answer=input()
    while not answer =="5": #if the answer is not five
        if answer=="1": #if it's one delete file
            os.remove(fileName)
        if answer=="2": #if two asks what user wants to add
            add=input("What do you want to add to your file? ")
            thisFile=open(fileName, "a")
            thisFile.write(add)
            thisFile.close()
        if answer=="3": #if three asks what user wants to write
            write=input("What do you want to write in your file? ")
            thisFile=open(fileName, "w")
            thisFile.write(write)
            thisFile.close()
        if answer=="4": #if four prints what is in file
            thisFile=open(fileName, "r")
            thisFile.read()
            thisFile.close()
        #asks user if they want to continue working on same file
        again=input("Do you want to do anything else with your file? (yes/no) ")
    #if answer not 1, 2, 3, 4, or 5 says to print one of them
    if not answer=="1" and not answer=="2" and not answer =="3" and not answer=="4" and not answer=="5":
        print("Please print a 1, 2, 3, 4, or 5. ")
        choices()
        answer=input()

create=input("Do you want to create a file? (yes/no) ") #asks if user wants to create a file
while create=="yes": #if answer is yes
    fileName=input("What do you want your file to be called? ") #asks for nameof file
    thisFile=open(fileName, "w")
    content=input("What information do you want your file to have? ") #asks what user wants to be in file
    thisFile.write(content)
    thisFile.close() #closes file
    choices() #print choices
    main() #prints main code
    if answer=="5": #if the answer
        create=input("Do you want to make another file? (yes/no) ") #asks if user wants to make a new file
    while again=="yes": #if the user wants to continue editing the file
        choices() #goes over all choices again
        answer==input()
        main()
    # if not again =="yes": #if they do not want to work on another file, ends
    #     break
