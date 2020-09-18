#Sarah Fradkin
#for number in range(5,0,-1): #goes by third number
#    print(number)
#for number in range(4,0,-1):
#    print(number)
#print ()

#CLASS loops : HOW TO DO

begin=5
lines=5 #5 numbers (lines 0,1,2,3,4)
for line in range(lines): #go from 0 to value
    for number in range(begin-line,0,-1): #begin(5) minus line, until 0 minus one
        print(number, end = ' ')
    print()
