import math
import collections

file1 = open('day10.txt', 'r')
lines = file1.readlines()
lines = list(map(lambda x: list(x.rstrip()) , lines))
validOpen = ['(', '[', '{', '<']

# counter = collections.Counter(syntax)
# sum = 0
# for brac, count in counter.items():
#     if brac == ')':
#         sum += count * 3
#     elif brac == ']':
#         sum += count * 57
#     elif brac == '}':
#         sum += count * 1197
#     else :
#         sum += count * 25137


syntax = []
for idx, chunk in enumerate(lines):
    stack = []
    for brac in chunk:
        if brac in validOpen:
            stack.append(brac)
        else: 
            # not an opening brac
            lastBrac = stack[-1]
            if brac == ')' and lastBrac == '(':
                stack.pop()
            elif brac == ']' and lastBrac == '[':
                stack.pop()
            elif brac == '}' and lastBrac == '{':
                stack.pop()
            elif brac == '>' and lastBrac == '<':
                stack.pop()
            else: 
                #wrong match
                stack = []
                break
    
    if stack != []: 
        # build sequence
        seq = []
        while stack:
            oBrac = stack.pop()
            if oBrac == '(':
                seq.append(')')
            elif oBrac == '[':
                seq.append(']')
            elif oBrac == '{':
                seq.append('}')
            else:
                seq.append('>')
        
        syntax.append(seq)

#print score
score = []
scoreBoard = {'}' : 3, ')': 1, ']': 2, '>':4 }
for seq in syntax:
    curr = 0
    for brac in seq:
        curr = curr * 5
        curr += scoreBoard[brac]
    
    score.append(curr)

print(sorted(score)[len(score)//2])
