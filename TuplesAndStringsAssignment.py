#Sarah Fradkin

 #1 create tuple
numbers=(3,7,12,4,6,32,8,9)

#2 tuple with different data
fruits_numbers=(3,7,1,9,0,"banana","apple","kiwi","lemon")

#3 print one number item
print(numbers[1])

#4 unpack tuple
sampletuple=(2,4,6,8) #new sample tuple
a,b,c,d=sampletuple #a=2 b=4 c=6 d=8 (gives each item variable)
print(a) #will print only 2

#5 adds number to tuple
numbers=numbers+(13,) # re-defines the tuple since tuples can't change

#6 converts tuple to string
numbers=str(numbers)

#7 prints fourth and fourth to last items
print(fruits_numbers[3]) # fourth item....
print(fruits_numbers[-4]) #\fourth from last item

#8 colon of a tuple
from copy import deepcopy #brings deepcopy from library(calls it, says we are about to use it)
tuplex=("hi",7,[],"apple") #creates random tuple with an array in it
tuplex_colon=deepcopy(tuplex)#makes a copy of tuplex using deepcopy
tuplex_colon[2].append(50) #addresses the array(index 2) and says to put 50 there
print(tuplex_colon) #prints the colon, with the 50

#9 find repeated item
tuple_repeat=(1,2,3,1,4,5,2,6) #creates a tuple with repeated items
count1=tuple_repeat.count(1) #assigns variable to count 1
print(count1) #prints how many times1 appears/repeats

#10 searches if there is a 9 in fruits_numbers
if 9 in fruits_numbers:
    print("9 was found")
else:
    print("9 not found")

#11 change list to tuple
list1=[1,2,3,4,5] #creates list
list1=tuple(list1) #changes list to tuple

#12 remove and item from a tuple
list2=list(fruits_numbers) # makes tuple a list so we can change things
list2.remove("apple") #removes apple
fruits_numbers=tuple(list2) #changes back into tple
print(fruits_numbers) #prints new tuple, now without apples

#13 slice a tuple
print(fruits_numbers[2:7]) #prints only that part of tuple(slices)

#14 finds index of items
index1=fruits_numbers.index(1) #in a tuple,find doesn't work so I have to do index
print(index1)

#15 length of tuple
print(len(fruits_numbers)) #prints length of tuple

#SKIP #16
# #16 convert tuple to dictionary
# tuplex1=(1,2,3,4,5)
# tuplex1=dict(tuplex1)
# print(type(tuplex1))

#17 unzip tuple
aList=[(1,2),(3,4),(5,6)] #list made up of tuple
print(list(zip(*aList))) #prints first element of each tuple in one tuple, and second element of each tuple in another one in a list
#(keeps in list(function(which list))

#18 reverse tuple
fruits_numbers=list(fruits_numbers) #converts to list
fruits_numbers.reverse() #reverses list
fruits_numbers=tuple(fruits_numbers) #converts back to tuple
print(fruits_numbers) #prints new tupple that is now reversed
