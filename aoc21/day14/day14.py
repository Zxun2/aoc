from collections import defaultdict, Counter
from itertools import pairwise
import functools
import math

from pprint import pprint


def p1(lines, p2=False):
    polymer_template = list(lines[0])
    pair_insertion = lines[2: ]
    pair_insertion = list(map(lambda x: tuple(x.split(' -> ')), pair_insertion))  
    pairs = {}
    for x, y in pair_insertion:
        pairs[x] = y


    for i in range(40):
        temp = polymer_template
        index = 1
        while index < len(polymer_template):
            pair = temp[index-1] + temp[index]
            if pair in pairs.keys():
                polymer_template.insert(index, pairs[pair])
                index += 2
            else: 
                index += 1
            

    counter = Counter(polymer_template)
    maxKey = max(counter, key=lambda x: counter[x])
    minKey = min(counter, key=lambda x: counter[x])

    return counter[maxKey] - counter[minKey]
    


def p2(lines):
    polymer = defaultdict(int)
    for pair in pairwise(lines[0]):
        polymer[pair] += 1

    pairs = defaultdict(str)
    for rule in lines[2:]:
        pairs[tuple(rule.split()[0])] = rule.split()[2]

    for i in range(1, 41):
        new_polymer = defaultdict(int)
        for pair in polymer:
            # if there are 10 exisiting (a, b) pairs i.e (a, b) : 10
            # 20 new pairs will be created
            # (a, c) : 10, (c, b) : 10
            new_polymer[(pair[0], pairs[pair])] += polymer[pair]
            new_polymer[(pairs[pair], pair[1])] += polymer[pair]
        # copy over
        polymer = new_polymer.copy()

    quantities = defaultdict(int)
    # Force first and last elements to be double counted for later logic
    # (pairwise means first and last were only counted once, such as
    # [AB, BC, CD, DE] leading to A and E only being included once each)
    quantities[lines[0][0]]  += 1 # first
    quantities[lines[0][-1]] += 1 # last
    for pair in polymer:
        quantities[pair[0]] += polymer[pair]
        quantities[pair[1]] += polymer[pair]

    # [AB, BC, CD] -> [AE, EB, BF, FC, CH, HD]
    # Everything is double counted except the first and last
    quantities = Counter(quantities).most_common()
    # All elements are double counted, so divide by 2 to get true counts
    return (quantities[0][1] - quantities[-1][1]) // 2

if __name__ == "__main__":
    file1 = open('day14.txt', 'r')
    lines = file1.readlines()
    lines = list(map(lambda x: x.rstrip(), lines))

    print(p2(lines))
    # print(p2(lines))