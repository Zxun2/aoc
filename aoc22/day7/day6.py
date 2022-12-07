from collections import Counter
def part1(): 
  with open("aoc22\day6\day6.txt", "r") as f:
    stream = "".join(f.readlines())
    counter = Counter(stream[:4])
    if len(counter.keys()) == 4: 
      return 0

    for idx, rp in enumerate(stream[4:]):
      if (left := counter.get(stream[idx]) - 1) == 0:
        del counter[stream[idx]]
      else:
        counter[stream[idx]] = left 
      
      counter.update(rp)
      if len(counter.keys()) == 4: 
        return idx + 1 + 4

def part2():
  with open("aoc22\day6\day6.txt", "r") as f:
    stream = "".join(f.readlines())
    counter = Counter(stream[:14])
    if len(counter.keys()) == 14: 
      return 0

    for idx, rp in enumerate(stream[14:]):
      if (left := counter.get(stream[idx]) - 1) == 0:
        del counter[stream[idx]]
      else:
        counter[stream[idx]] = left 

      counter.update(rp)
      if len(counter.keys()) == 14: 
        return idx + 1 + 14


if __name__ == "__main__":
  print(part1())
  print(part2())