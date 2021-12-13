import collections

file1 = open('day6.txt', 'r')
lines = file1.readlines()
fishes = list(map(lambda x: int(x) , lines[0].split(',')))

#part 1
i = 1
prev = 0
numZeroes = 0
while i < 256:
    fishes = list(map(lambda x: x-1, fishes))
    # print(f'day{i}, {fishes}')
    for j in range(len(fishes)):
        if fishes[j] == 0:
            numZeroes += 1
            fishes[j] = 7
    
    numOfEight = numZeroes - prev
    for k in range(numOfEight):
        fishes.append(9)

    prev = numZeroes
    i+= 1

# part 2
new = collections.Counter(fishes)
for i in range(256):
    temp = collections.Counter()
    for p in new:
        if p-1 == -1:
            temp[6] += new[p]
            temp[8] += new[p]
        else:
            temp[p-1] += new[p]
    
    new = temp.copy()
print(sum(new.values()))

