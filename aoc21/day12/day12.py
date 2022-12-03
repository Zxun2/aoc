import math
import collections
from typing import DefaultDict


def solve(): 
    dict = DefaultDict(list)
    file1 = open('day12.txt', 'r')
    lines = file1.readlines()
    lines = list(map(lambda x: x.rstrip().split('-') , lines))

    for key, value in lines:
       dict[key].append(value)
       dict[value].append(key)

    routes = 0 
    start = ('start', set(['start']), None)
    stack = collections.deque([start])
        
    while stack:
        pos, cow, seen = stack.popleft()
        if pos == 'end':
            routes += 1 
            continue

        for y in dict[pos]:
            if y not in cow:
                new_cow = set(cow)
                if y.lower() == y:
                    new_cow.add(y)
                stack.append((y, new_cow, seen))
            elif y in cow and seen is None and y not in ['start', 'end']:
                stack.append((y, cow, y))

    print(routes)



solve()