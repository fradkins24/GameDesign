# Sarah Fradkin

#print("1\n" + "2\n" + "3\n"+ "4\n")
#print("1\n")
#print("2 2\n")
#print("3 3 3\n")

#for i in range(10):# value from 0 to value-1 (9)
#    print (i)
#for j in range (1,10): # first number is included, second is not
#    print (j, end = '') #prints j horizontally
#    print (" ", end = '') #prints a space
#print ()
#print("I am done")
# print("...")

#nested loops
#for line in range (1,10):
    #for number in range(line):#variable in first loop controls second loop
        #print(line, end = '')
    #print()

#challenge/homework
for line in range (1,10):
    for space in range (9-line):
        print(" ", end = '')
    for number in range (line):
        print (line, end = '')
        
    for number in range (line):
        print (line, end = '')
    print ()
