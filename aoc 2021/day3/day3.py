import collections

file1 = open('day3.txt', 'r')
Lines = list(map(lambda x: x.rstrip(), file1.readlines()))

ogr = []
co2 = []
dict = collections.defaultdict(dict)


pos = 0 
max_length = len(Lines[0])
temp_Arr = Lines

# while pos < max_length:  
#     for binaryString in temp_Arr:
#         bit = binaryString[pos]         
#         newDict = dict[pos]
#         if bit not in newDict.keys():
#             newDict[bit] = 1
#         else:
#             newDict[bit] += 1

#     maxBit = max(dict[pos], key=lambda x: dict[pos][x])
#     minBit = min(dict[pos], key=lambda x: dict[pos][x])

#     if len(dict[pos]) > 1 and dict[pos]["0"] == dict[pos]["1"]: 
#         ogr.append("1")
#     else: 
#         ogr.append(maxBit)
#     arr = []

#     for binaryString in temp_Arr:
#         bit = binaryString[pos] 
#         if bit == ogr[-1]:
#             arr.append(binaryString)

#     temp_Arr = arr
#     print(temp_Arr)
#     pos += 1

while pos < max_length:  
    for binaryString in temp_Arr:
        bit = binaryString[pos]         
        newDict = dict[pos]
        if bit not in newDict.keys():
            newDict[bit] = 1
        else:
            newDict[bit] += 1

    maxBit = max(dict[pos], key=lambda x: dict[pos][x])
    minBit = min(dict[pos], key=lambda x: dict[pos][x])

    if len(dict[pos]) > 1 and dict[pos]["0"] == dict[pos]["1"]: 
        ogr.append("0")
    else: 
        ogr.append(minBit)
    arr = []

    for binaryString in temp_Arr:
        bit = binaryString[pos] 
        if bit == ogr[-1]:
            arr.append(binaryString)

    temp_Arr = arr
    print(temp_Arr)
    pos += 1
    
ogr = ''.join([str(elem) for elem in ogr])
print(int(ogr, 2))

# print(int(ogr, 2) * int(co2, 2))
print(1639 * 2692)