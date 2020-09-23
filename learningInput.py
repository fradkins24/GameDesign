# Sarah Fradkin
# learing how to resize our programs
# asking the user for input
# input is requesting via console for something: the default is string
# type casting (forcing something to be a type of data)

#begin = int(input('Number in lines\n'))
#lines=5
#for line in range(lines):
#    for number in range(begin-line,0,-1):
#        print(number, end = ' ')
#    print ()

#NUMBERS PYRAMID

for line in range (1,9):
    for space in range (8-line):
        print(" ", end = '')
    for number in range (line,0,-1): # goes all the way until 0, going down by one
        print (number, end = '')
    for number in range(2,line+1): #starts at 2 and goes until the line+1 (so that the last number is the line)
        print(number, end = '')
    print()
