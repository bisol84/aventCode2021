#Main variables
nbrAdd = int(0)
tempArray = list()

#Read the input file
with open('./input.txt','r') as f:
    for i in f.readlines():
        tempArray.append(int(i.strip("\n")))

#Loop in the list
for i in range(len(tempArray)):
    if sum(tempArray[i+1:i+4]) > sum(tempArray[i:i+3]):
        nbrAdd += 1

print('Résultat : ', nbrAdd)