#Sarah Fradkin
#10/28/2020
# learning about files
# open/create
# close
# write      "w"
# append     "a"
# read       "r"
#create a file variable name=open("fileName.txt", function)
#to be able to remove a file we need to use the OS (operating system) module
myFile= open("newFile.txt", "w") #opens file if exists, if not it will create a file
import os, time
myFile.write("I am adding some stuff")
myFile.close()
myFile=open("newFile.txt","r")
print(myFile.read())
myFile.close()
myFile= open("newFile.txt", "w") #iuse w it will replace what is already in the file
myFile.write("Opps, I deleted my stuff\n")
myFile.close()
myFile=open("newFile.txt","r")
print(myFile.read())
myFile.close()
myFile= open("newFile.txt", "a") #adds to file
myFile.write("I add more stuff")
myFile.close()
myFile=open("newFile.txt","r")
print(myFile.read())
myFile.close()
time.sleep(5)
if os.path.exists("List-tupleArrays.py"): #check if a file exists in he same folder as the file created
    print("yes")
else:
    print("no")
#os.remove("newFile.txt") #deletes file
myFile=open("lineFile.txt","w")
for i in range(10):
    word="this is line #"+str(i+1)+"\r\n"
    myFile.write(word)
myFile.close()
myFile=open("lineFile.txt","r")
print(myFile.read())
myFile.close()
os.remove("lineFiles.txt")
