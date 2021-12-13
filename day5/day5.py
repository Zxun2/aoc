file1 = open('day5.txt', 'r')
lines = list(map(lambda x: x.rstrip(), file1.readlines()))

arr = []
max_X = 0
max_Y = 0
for i in lines:
    line = i.split(' -> ')
    coord = list(map( lambda x: tuple(x.split(',')) , line))  #[('0', '9'), ('5', '9')]
    
    for coo in coord: 
        max_X = max(int(coo[1]), max_X)
        max_Y = max(int(coo[0]), max_Y)

    arr.append(coord)


diagram = [ [0]*(max_Y+1) for i in range(max_X+1)] 
rows = len(diagram)
cols = len(diagram[0])

def draw_line(coord):
    left_x = int(coord[0][0])
    left_y = int(coord[0][1])

    right_x = int(coord[1][0])
    right_y = int(coord[1][1])

    if left_x == right_x:
        # vertical line
        start = min(left_y, right_y)
        end = max(left_y, right_y)
        

        for i in range(start, end+1):
            diagram[i][left_x] += 1

    elif left_y == right_y:
        # horizontal line
        start = min(left_x, right_x)
        end = max(left_x, right_x)

        for i in range(start, end+1):
            diagram[left_y][i] += 1
    else: 
        #diagonal line
        left = (left_x, left_y) 
        right = (right_x, right_y)

        if left_x == left_y and right_x == right_y:
            start = min(left_x, right_x)
            end = max(left_x, right_x)

            for i in range(start, end+1):
                diagram[i][i] += 1
        
        elif (left_x > right_x and left_y > right_y) or (right_x > left_x and right_y > left_y):
            left = (left_x, left_y) 
            right = (right_x, right_y)

            start = min(left, right, key = lambda l : l[1])
            end = max(left, right, key = lambda l : l[1])
            

            ro = start[1]
            co = start[0]
            while ro <= end[1] :
                diagram[ro][co] += 1
                ro += 1
                co += 1
        else: 
            left = (left_x, left_y) 
            right = (right_x, right_y)


            start = min(left, right, key = lambda l : l[1])
            end = max(left, right , key = lambda l : l[1])

            ro = start[1]
            co = start[0]
            while ro <= end[1] :

                diagram[ro][co] += 1
                ro += 1
                co -= 1


for line in arr:
    draw_line(line)

counter = 0
for i in range(rows):
    for j in range(cols):
        if diagram[i][j] > 1:
            counter += 1

print(counter)

