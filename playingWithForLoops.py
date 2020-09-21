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
#for number in range(start,end):
#    if number%2==1:
#        if number%3==0:
#            print('',end = '')
#        elif number%5==0:
#            print('',end ='')
#        elif number%7==0:
#           print('',end = '')
#        else:
#            print (number)

# Fibonacci CHALLENGE ASSIGNMENT

f1=0
f2=1
print (f1,end = ' ')
print (f2, end = ' ')
for number in range (0,8):
    f3=f1+f2
    print (f3, end = ' ')
    f1=f2 # re-assigns f1
    f2=f3 # re-assigns f2 and repeats loop with new variables
