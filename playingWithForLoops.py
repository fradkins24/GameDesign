#Sarah Fradkin
#for number in range(5,0,-1): #goes by third number
#    print(number, end = ' ')
#print ()
#for number in range(4,0,-1):
#    print(number, end = ' ')
#print ()
#for number in range(3,0,-1):
#    print(number, end = ' ')
#print()
#for number in range(2,0,-1):
#    print (number, end = ' ')
#print ()
#for number in range(1,0,-1):
#    print(number)

#CLASS loops : HOW TO DO

#begin=5
#lines=5 #5 numbers (lines 0,1,2,3,4)
#for line in range(lines): #go from 0 to value
#    for number in range(begin-line,0,-1): #begin(5) minus line, until 0 minus one
#        print(number, end = ' ')
#    print()

 #PRIME CHALLENGE ASSIGNMENT

#start=25
#end=50
#for number in range(start,end): # prints for numbers between 25,49
#    if number%2==1: #if it is odd continue
#        if number%3==0: # if is divided evenly by three
#            print('',end = '') #print nothing
#        elif number%5==0: # if not, then continue to if it divided by 5 evenly and so on...
#            print('',end ='')
#        elif number%7==0:
#           print('',end = '')
#        else:
#            print (number) # after going through the guidlines, if it passes all og them, the number will be printed and the loop repeats with each number

# Fibonacci CHALLENGE ASSIGNMENT

f1=0 # first number in fibonacci code
f2=1 # second number in fibonacci code
print (f1,end = ' ') # prints first number of fibonacci code to start it off
print (f2, end = ' ') # print second number of fibonacci code to also start it off
for number in range (0,8): # prints eight number, repeats each time by adding last two numbers
    f3=f1+f2 # adds last two numbers printed
    print (f3, end = ' ')
    f1=f2 # re-assigns f1
    f2=f3 # re-assigns f2 and repeats loop with new variables
