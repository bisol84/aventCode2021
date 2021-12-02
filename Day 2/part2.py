#Variables
horizontal = int(0)
depth = int(0)
aim = int(0)

#Read the file
with open('./input.txt','r') as f:
    for line in f:
        splitedLine = line.split(' ')
        information = splitedLine[0]
        number = int(splitedLine[1])

        if information == 'forward':
            horizontal += number
            depth = depth + (number * aim)
        elif information == 'down':
            aim += number
        elif information == 'up':
            aim -= number

print('result : ', horizontal * depth)