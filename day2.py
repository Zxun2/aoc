file1 = open('day2.txt', 'r')
Lines = list(map(lambda x: x.split(), file1.readlines()))

aim = 0
horizontalPos = 0
depth = 0

commands = ['forward', 'down', 'up']

for direction, units in Lines:
    if direction in commands:
        if direction == 'forward': 
                horizontalPos += int(units) 
                depth += aim * int(units)
        elif direction == 'down': 
                aim += int(units)
        else:
            aim -= int(units)


print(horizontalPos * depth)