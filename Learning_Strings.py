# Sarah Fradkin
# string: an array of characters
# last index of array is len-1
#EXAMPLE

# strVar = "My name is M"
# print(strVar)
# print(len(strVar)) #you get the length of the srting
# print(strVar[len(strVar)-1]) #prints last index but printing the length minus one, and the index in that place
# #print(strVar[0:5]) #will print first four digits (includes first numbe, but not last)
# indexNum=(strVar.find("name"))
# print(indexNum) #will print the number in which the first index of "name" is
# print(strVar[indexNum:indexNum+4])
# print(strVar[indexNum:]) #prints from first number, to end (works both ways)
# print(strVar[:indexNum])
# print(strVar.replace('name','inital')) #replaces first thing with second
# strVar=strVar.replace('name','inital') #this makes it perminant because the = indicates you changing it
# print(strVar)
# print(strVar.upper()) #always need extra (), but since they are blank it means no parameters: prints all
# print(strVar.lower())
# strVar=strVar.upper() #makes it permanent
# print(strVar)
# print(list(strVar)) #list breaks the array apart into individual indexes
# back = list(strVar)
# # back = back.reverse()
# # print(' '.join(back))


#HOMEWORK string

mainStr = "Here are the instructions to install Drivers\n" "1. After the download is completed go to where you saved the folder.\n""(By default everything you download from the Internet is saved to the Downloads folder)\n""2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.\n""3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.\n""4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:\n""*setup application\n""*Asussetup\n""*pnpinstal64\n""*pnputil\n""*Igxpin\n""5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up.\n"

strVar=mainStr
word_count= 0
lenD=len("Drivers") #length of drivers
lenVar=len(strVar) #length of string
for i in range(lenVar): #goes to the length of the string(searches entire string)
    indexDrive=(strVar.find("Drivers")) #trying to find how many times the word Drivers appears (inside loop so that is searches each time it repeats)
    if indexDrive > 0: #if there is an index(drivers is found)
        word_count=word_count+1 #add 1 to the word_count each time drivers is found
        strVar=strVar[indexDrive+lenD:] #re-assigns strVar (which also re-assigns length) so that it starts after drivers is found and continues until the end
print(word_count) #once the loop is done, word_count will be printed, which should be the amount of times drivers appeared

print(len(mainStr)) #prints length of string

print(mainStr.replace('Extract', 'EXTRACT')) #replaces Extract with EXTRACT

print(mainStr.replace('setup','SETUP')) #replaces setup with setup

index4=(mainStr.find("4")) #finds in which index 4 is
print(index4)

indexEnter=(mainStr.find("\n")) #finds first \n or first enter
print(indexEnter)

str1=mainStr
index1=(str1.find("1.")) #finds 1.
print(str1[index1:index1+2], end= '') #prints value of index1 to value of index1+2 so that it prints 1.
str1=str1[index1+2:] #changes str1 to erase everything before the 1.
indexDot=(str1.find(".")) #finds value of . in the NEW str1
print(str1[:indexDot+1])#prints from beginning of new str1 to indexDot+1 so that it is included

str2=mainStr
index2=(str2.find("2.")) #finds 2.
print(str2[index2:index2+2], end= '') #prints value of index2 to value of index2+2 so that it prints 2.
str2=str2[index2+2:] #changes str2 to erase everything before the 2.
indexDot=(str2.find(".")) #finds value of . in the NEW str2
print(str2[:indexDot+1])#prints from beginning of new str2 to indexDot+1 so that it is included

str3=mainStr #same resoning as 1 and 2
index3=(str3.find("3."))
print(str3[index3:index3+2], end= '')
str3=str3[index3+2:]
indexDot=(str3.find("."))
print(str3[:indexDot+1])

str4=mainStr #same resoning as 1 and 2
index4=(str4.find("4."))
print(str4[index4:index4+2], end= '')
str4=str4[index4+2:]
indexDot=(str4.find("."))
print(str4[:indexDot+1])

str5=mainStr #same resoning as 1 and 2
index5=(str5.find("5."))
print(str5[index5:index5+2], end= '')
str5=str5[index5+2:]
indexDot=(str5.find("."))
print(str5[:indexDot+1])
