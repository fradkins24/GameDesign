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
dict1={"fruit":"apple","number":1}
#print(dict1.sort())

#2 add key to dictionary
dict1["vegatable"]="eggplant" #adds new entry/key
print(dict1)

#3 concatenate (add, link) dictionaries together
dict2={"a":1,"b":2}
dict3={"c":3,"d":4}
dict2.update(dict3) #updates dict2 to make it both
print("%s"%dict2) #ASK WHAT THI MEANS
