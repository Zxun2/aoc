import collections
from typing import Counter
import itertools
"""
# 0: 6
# 6: 6
# 9: 6
# 2: 5
# 3: 5
# 5: 5
# UNIQUE #
# 8: 7
# 4: 4
# 7: 3
# 1: 2
"""

# Part 1
file1 = open('day8.txt', 'r')
# lines = file1.readlines()
# lines = list(map(lambda x: x.split(' | ')[1].rstrip().split(' '), lines))
# lines = list(itertools.chain(*lines))
# flat_lines = len(list(filter(lambda x: len(x) == 7 or len(x) == 4 or len(x) == 3 or len(x) == 2, lines)))

# Part 2
lines_2 = file1.readlines()
lines_2 = list(map(lambda x: x.split(' | '), lines_2))
'''
(acedgfb : 8) cdfbe gcdfa fbcad (dab : 7) 
cefabd cdfgeb (eafb : 4) cagedb (ab : 1) | 

cdfeb fcadb cdfeb cdbaf

len 6: (9 : 4), len 6: (0 : 1) (6 : 1), len 5: 2 odd, (3 : 1), (5: 6)
'''
sum = 0
for line in lines_2:
    signals = line[0].split(' ')
    outputs = line[1].rstrip().split(' ')

    hash = {}
 
    # figuring out 9 using 4
    num4 = list(filter( lambda x: len(x) == 4, signals))
    num4 = list(num4[0])
    hash[''.join(sorted(num4))] = 4

    len_6 = list(map(lambda x: list(x), filter( lambda x : len(x) == 6, signals)))
    i = 0 
    while i < len(len_6):
        boolean = True
        signal = len_6[i]
        for j in num4:
            boolean = boolean and (j in signal)
        
        if boolean: 
            break
        i += 1

    hash[''.join(sorted(len_6[i]))] = 9
    len_6.pop(i)

    # figuring 0 and 6
    num1 = list(filter( lambda x: len(x) == 2, signals))
    num1 = list(num1[0])
    hash[''.join(sorted(num1))] = 1

    k = 0
    while k < len(len_6):
        boolean = True
        signal = len_6[k]
        for j in num1:
            boolean = boolean and (j in signal)
        
        if boolean: 
            break
        k += 1

    hash[''.join(sorted(len_6[k]))] = 0
    hash[''.join(sorted(len_6[(k+1) % 2]))] = 6
    number6 = len_6[(k+1) % 2]
    
    # figuring 3
    len_5 = list(map(lambda x: list(x), filter( lambda x : len(x) == 5, signals)))
    T = 0
    while T < len(len_5):
        boolean = True
        signal = len_5[T]
        for j in num1:
            boolean = boolean and (j in signal)
        
        if boolean: 
            break
        T += 1

    hash[''.join(sorted(len_5[T]))] = 3
    len_5.pop(T)
    # figuring 5
    Y = 0
    while Y < len(len_5):
        boolean = True
        print(number6)
        signal = number6
        print(Y)
        for j in len_5[Y]:
            boolean = boolean and (j in signal)

        if boolean == True:
            break
        else: 
            Y += 1

    print(len_5, Y)


    hash[''.join(sorted(len_5[Y]))] = 5
    # figuring 2
    hash[''.join(sorted(len_5[(Y + 1) % 2]))] = 2

    num = ''
    for i in outputs:
        if len(i) == 7:
            num += '8'
        elif len(i) == 3:
            num += '7'
        else:
            key = ''.join(sorted(list(i)))
            num += str(hash[key]) 
    print(hash)
    sum += int(num)
print(sum)