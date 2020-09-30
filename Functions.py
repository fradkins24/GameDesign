# Sarah Fradkin
#learning abour functions
# functions: chunks of program that we can call when we need them
def testing_Functions(): #defin(def) the function and expects no parameters
    #print("1\n" + "2\n" + "3\n"+ "4\n")
    print("1\n")
    print("2 2\n")
    print("3 3 3\n")
def running_Loops(lines):
    line=int(lines)
    for i in range(line):# value from 0 to value-1 (9)
       print (i)
    for j in range (1,line): # first number is included, second is not
       print (j, end = '') #prints j horizontally
       print (" ", end = '') #prints a space
    print () #used as an enter
    print("I am done")
    print("...")
def loop_rows_col(row, col):
    for rows in range(row):
        for cols in range(col):
            print('*', end ='') #print number of rows and number of columns of *
        print()

#start of main program

loop_rows_col(5,7)
# running_Loops(7)
# for y in range (3):
#     testing_Functions() #this is calling the function, meaning after it prints the x, it will print whatever is n the function
