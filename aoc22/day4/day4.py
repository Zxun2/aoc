def part1(): 
  count = 0
  with open("aoc22\day4\day4.txt", "r") as f:
    for i, val in enumerate(f.readlines()):
      val = val.rstrip()
      val = val.split(",")
      val = list(map(lambda x: x.split('-'), val))

      val = list(map(lambda x: list(map(lambda y: int(y), x)), val))
      pairs = list(map(lambda x: set(range(x[0], x[1] + 1)), val))
      
      if pairs[0].issubset(pairs[1]) or pairs[1].issubset(pairs[0]):
        count += 1 

  print(count)

def part2():
  count = 0
  with open("aoc22\day4\day4.txt", "r") as f:
    for i, val in enumerate(f.readlines()):
      val = val.rstrip()
      val = val.split(",")
      val = list(map(lambda x: x.split('-'), val))

      val = list(map(lambda x: list(map(lambda y: int(y), x)), val))
      pairs = list(map(lambda x: set(range(x[0], x[1] + 1)), val))
      
      if pairs[0].intersection(pairs[1]):
        count += 1

  print(count)

if __name__ == "__main__":
  part1()
  part2()