# Sarah Fradkin
#SETS
thisset={"apple","banana","cherry"} #sets re not ordered or indexed (will be in different order each time printed)
for x in thisset:
    print(x)
print("banana" in thisset) #if there is a banana, says true, otherwise, says False
if("kiwi" in thisset): # If there is a kiwi:
    thisset.add("orange") #with add you can only add one element
else:
    thisset.update({"mango","berries","kiwi"}) #with update you can add multiple but as a set of elements (set, list, tuple)
for x in thisset:
    print(x)
print(len(thisset)) #even if it is not indexed, it still has a length
otherset={1,2,3,4}
anotherset={"kiwi","mango","papaya","watermelon"}
print(thisset.union(otherset)) #adds sets together
print(thisset.intersection(anotherset)) #prints elements that both have

#DICTIONARIES
myDictionary={"Name1":"Peter", "Age1":18, "School1":"Greenhill"} #definition of key name1 is peter because of:
print("The name of the student is",myDictionary["Name1"]) #prints string, then definition of name 1
print(myDictionary.keys())



#DICTIONARY ASSIGNMENT

#1 sort a dictionary (acsending and decsending) by value
ages= {"Lily":6,"Talia":9,"Stacy":3,"Rachel":7}
#ascending
sort_ages = sorted(ages.items(), key=lambda x: x[1]) #sorts every item in ages ***ASK WHAT ISAFTER ITEMS***
for i in sort_ages: #creates a loop to sort
	print(i[0], i[1]) #ASK WHAT THIS MEANS
#descending
sort_ages = sorted(ages.items(), key=lambda x: x[1],reverse=True) #sorts every item in ages ***ASK WHAT ISAFTER ITEMS***
for i in sort_ages: #creates a loop to sort
	print(i[0], i[1]) #ASK WHAT THIS MEANS

#2 add key to dictionary
dict1={"fruit":"apple","number":1}
dict1["vegatable"]="eggplant" #adds new entry/key
print(dict1)

#3 concatenate (add, link) dictionaries together
dict2={"a":1,"b":2}
dict3={"c":3,"d":4}
dict2.update(dict3) #updates dict2 to make it both
print("%s"%dict2) #ASK WHAT THIS MEANS

#4 check if key exists
thisdict={"name":"Sarah","age":14}
if "name" in thisdict: #if there is a key called name
    print("My name is",thisdict["name"]) #print this
else: #if not
    thisdict["name"]="Sarah" #add it

#5 print dictionary using for loop
mydict={"one":1,"two":2,"three":3}
for x,y in mydict.items(): #for items x and y in mydict
    print(x,y) #print the items x and y

#6 squares of numbers between 1 and n
n=3 #declare variable
dicta={} #create empty dict
for i in range(1,n+1): #make loop with variable i between 1 and n
    dicta[i]=i*i #adds a key(i) and makes the value the square of i
print(dicta) #prints resulting dict

#7 numbers 1-15 squared
dictb={} #same logic as 6
for m in range(1,16):
    dictb[m]=m*m
print(dictb)

#8 merge dicts
#LOOK AT #3

#9 iterate(print) using for loop
#LOOK AT #5

#10 sum of items
fruits={"apples":1,"bananas":6,"kiwis":4,"strawberries":12}
print("We have",sum(fruits.values()),"fruits.") #prints sum of values (how many fruits)
