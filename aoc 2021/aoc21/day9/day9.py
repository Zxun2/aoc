import math

file1 = open('day9.txt', 'r')
lines = file1.readlines()
lines = list(map(lambda x: list(x.rstrip()) , lines))

# right left down up
neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0)]
arr = []

rows = len(lines)
cols = len(lines[0])
for i in range(rows):
    for j in range(cols):
        state = True
        for row, col in neighbours:
            if  0 <= i + row < rows and 0 <= j + col < cols:
                lt = int(lines[i][j]) < int(lines[i + row][j +col])
                state = state and lt
        if state:
            arr.append((i, j))


sizes = []

print(arr)

for r,c in arr:
    queue = []
    temp = 0
    queue.append((r, c))
    while queue:
        # print(queue)
        row, col = queue.pop(0)
        if lines[row][col] == "-1":
            continue
        lines[row][col] = "-1"
        temp += 1
        for rr, cc in neighbours:
            rv, cv = row + rr, col + cc
           
            if  rv >= 0 and rv < rows and cv >= 0 and cv < cols:
                if lines[rv][cv] == '9' or lines[rv][cv] == "-1":
                    continue
                else:
                    if row == 1 and col == 9:
                        print(rv, cv)
                    queue.append((rv, cv))

            
    sizes.append(temp)


print(math.prod(sorted(sizes)[-3:]))
