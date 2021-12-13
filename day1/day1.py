# Using readlines()
file1 = open('day1.txt', 'r')
Lines = list(map(lambda x: int(x), file1.readlines()))

count = 0
arr = []

for i in range(len(Lines)):
    operand1 = Lines[i]
    operand2 = Lines[i+1] if i+1 < len(Lines) else False
    operand3 = Lines[i+2] if i+2 < len(Lines) else False
    iterable = [operand1, operand2, operand3]
    if all([operand1, operand2, operand3]): 
        arr.append(sum(iterable))


first_elem = arr[0]
for idx in range(1, len(arr)):
    if arr[idx] > arr[idx-1]:
        count += 1

print(count)