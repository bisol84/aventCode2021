#Main variables
prevNumber = int(0)
resultList = list()

#Read the input file
with open('./input.txt','r') as f:
    for line in f:
        if int(line) > int(prevNumber):
            resultList.append(int(line))

        prevNumber = int(line)

print(len(resultList) - 1)    
