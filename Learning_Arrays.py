#Sarah Fradkin
#learning arrays
names=["Ali", "Justin", "Daniel", "Jake", "Rohan", "Sarah", "August", "Aarian", "Kunal", "Safin"]
#        0       1         2         3       4        5        6          7        8        9
#print(names) #becasue it's an array, it prints exactly whatnames is (with the brackets)
#print(names[2]) #prints value in the 2 index
for i in range(len(names)): #len is length
    print(names[i]) #the i is the index, without it won't do what you want
fruits=["apples", "oranges", "bananas"]
for foods in range(len(fruits)):
    print(fruits[foods], end =',')
