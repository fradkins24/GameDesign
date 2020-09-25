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

#for line in range (1,9):
#    for space in range (8-line):
#        print(" ", end = '')
#    for number in range (line,0,-1): # goes all the way until 0, going down by one
#        print (number, end = '')
#    for number in range(2,line+1): #starts at 2 and goes until the line+1 (so that the last number is the line)
#        print(number, end = '')
#    print()


#STAR SHAPE

end= 9
for line in range(1,end):
    for star in range(line): #print number of stars as number of line (line 1 - one star)
        print("*", end = '')
    for space in range(end-1-line):# prints spaces according to line(line 2 - 6 spaces)
        print(' ', end = '')
    for star in range (end+1-line): #prints stars according to line (line 3 - 7 stars)
        print ("*", end = '')
    for space in range(line*2-2): # multiplys line by two, subtracts two, and then prints hat many spaces (line 4 - 6 spaces)
        print(" ", end = '')
    for star in range (end-line): #prints stars according to line (line 5 - 4 stars)
        print("*", end = '')
    for space in range (end-1-line): # prints spaces according to line (line 6 - 2 spaces)
        print (" ", end = '')
    for star in range (line): #prints number of stars as number of line (line 7 - 7 stars)
        print ("*", end = '')
    print ()
