#Sarah Fradkin
myList=[2,4,5,7,8,9]
numbers=(3,4,8,2,1) #tuple
if 2 in numbers:
    print("I love tuples")
print(numbers[1:4])
yourList=[98,87,65]
myFruit=["apple","banana","orange"]
newFruit=myFruit.copy() #copies array how it is now
#myFruit.remove("apple") #removes word (apple) from list
myFruit.pop(0) #removes what is in the space the index (method)
del myFruit[0] #removes what is in the space the index (function)
#del myFruit #removes entire array
# print(myList[1])
# print(myList[-2]) #starts from back with no 0
myFruit.append("mango") #will add to the end of the array
myFruit.insert(1,"kiwi") #first value is in what index you want to add the second value
print(myFruit)
newFruit.clear() #clears what is in the array without deleting it
newFruit.append("strawberry")
print(newFruit)
if 4 in myList: #easy way to find if something is in the array
    print("yes")
if "banana" in myFruit:
    print("I love banana")
if "berries" in myFruit:
    print("I love berries")
else:
    print("buy some berries")
# for x in myList: #since it's an array, we don't need to say in range
#     print(x)

# JOINING LISTS
#ourList=myList+myFruit # creating new list that adds lists together
#print(ourList)
# for i in myFruit:
#     myList.append(i) #changes original list
# print(myList)
myList.extend(myFruit) #canges original list
print(myList)
#myList.sort() #typecast before you sort
myFruit.sort() #sorts it(alphabetical)
print(myFruit)
