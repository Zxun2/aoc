import math
import collections


def solve(): 
    file1 = open('day11.txt', 'r')
    lines = file1.readlines()
    lines = list(map(lambda x: list(x.rstrip()) , lines))
    lines = list(map(lambda x: list(map(lambda y: int(y), x)), lines))
    rows = len(lines)
    cols = len(lines[0])
    neighbour = [(0, 1), (1, 0), (-1, -1), (1, 1), (-1, 0), (0, - 1), (-1, 1), (1, -1)]
    # numFlashes = 0
    step = 0

    while True:
        flashed = set()
        stack = []
        for i in range(rows):
            for j in range(cols):
                #add one to each value
                if (i, j) not in flashed:
                    lines[i][j] = (lines[i][j] + 1) % 10
                    if lines[i][j] == 0: #flashes
                        # numFlashes += 1
                        stack.append((i, j))
                        #add one to adjacent tiles
                        flashed.add((i, j)) #add flashed
                        while stack: 
                            x, y = stack.pop(0)
                            for r, c in neighbour:
                                rr = x + r
                                cc = y + c
                                if rr >= 0 and rr < rows and cc >= 0 and cc < cols and (rr, cc) not in flashed:
                                    lines[rr][cc] = (lines[rr][cc] + 1) % 10
                                    if lines[rr][cc] == 0: #flashes
                                        # numFlashes += 1
                                        stack.append((rr, cc))
                                        flashed.add((rr, cc))

        if len(flashed) == rows*cols:
            step += 1
            break
        step += 1
        
    print(step)



solve()