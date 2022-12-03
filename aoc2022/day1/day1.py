def part1():
  # Using readlines()
  file1 = open('aoc2022\day1\day1.txt', 'r')
  arr = []
  rolling_sum = 0
  for i, val in enumerate(file1.readlines()): 
    if val == "\n":
      arr.append(rolling_sum)
      rolling_sum = 0 # reset
    else:
      rolling_sum += int(val)      
  
  print(max(arr))
  return arr


def part2():
  arr = part1()
  arr = sorted(arr)
  print(sum(arr[-3: ]))
  

if __name__ == "__main__":
  part2()