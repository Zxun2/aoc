import collections
from typing import Counter

# file1 = open('day7.txt', 'r')
# lines = file1.readlines()
# lines = list(map(lambda x: int(x) , lines[0].split(',')))

# # # temp = Counter(lines)
# # # pos = max(temp, key= lambda x: temp[x])
# arr = []
# min_pos = min(lines)
# max_pos = max(lines)


# for i in range(min_pos, max_pos+1):
#     cost = 0 
#     for j in lines:
#         n = abs(j - i)
#         cost += (n * (n+1))/2
#     arr.append(cost)

# print(min(arr))

my_file = open("day7.txt", "r")
position = list(map(lambda x: int(x), my_file.readline().strip().split(',')))

def new_distance(y):
    sum = (y/2) * (2 + (y - 1))
    return sum

def distance(x):
    distance = 0
    for num in position:
        distance += new_distance(abs(num - x))
    return distance

lst = []
minimum = min(position)
maximum = max(position)
for i in range(minimum, maximum + 1):
    lst.append(distance(i))

minimum_value = min(lst)
minimum_index = lst.index(minimum_value)
value = minimum_index + minimum

print(minimum_value)