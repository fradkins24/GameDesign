#Sarah Fradkin

 #1 create tuple
numbers=(3,7,12,4,6,32,8,9)

#2 tuple with different data
fruits_numbers=(3,7,1,9,0,"banana","apple","kiwi","lemon")

#3 print one number item
print(numbers[1])

#5 adds number to tuple
numbers=numbers+(13,) # re-defines the tuple since tuples can't change

#6 converts tuple to string
numbers=str(numbers)

#7 prints fourth and fourth to last items
print(fruits_numbers[3]) # fourth item....
print(fruits_numbers[-4]) #\fourth from last item

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

#15 length of tuple
print(len(fruits_numbers))
