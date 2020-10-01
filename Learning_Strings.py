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

strVar = "Here are the instructions to install Drivers\n" "1. After the download is completed go to where you saved the folder.\n""(By default everything you download from the Internet is saved to the Downloads folder)\n""2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.\n""3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.\n""4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:\n""*setup application\n""*Asussetup\n""*pnpinstal64\n""*pnputil\n""*Igxpin\n""5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up.\n"

indexDrive=(strVar.find("Drivers")) #trying to find how many times the word Drivers appears
word_count= 0
len2=len("Drivers")
len1=len(strVar)
i=0
for i in range(i,len1):
    if indexDrive > 0:
        word_count=word_count+1
        i=indexDrive+len2
    else:
        print("Not Found")
print(word_count)


#print(len(strVar)) #prints length of string
#
#print(strVar.replace('Extract', 'EXTRACT')) #replaces Extract with EXTRACT

# print(strVar.replace('setup','SETUP')) #replaces setup with setup

# index4=(strVar.find("4")) #finds in which index 4 is
# print(index4)

#indexEnter=(strVar.find("\n")) #finds first \n or first enter
# print(indexEnter)

# index1=(strVar.find("1")) #trying to print from one until the end of the statement
# indexDot=(strVar.find("."))
# print(strVar[index1:indexDot+1])
