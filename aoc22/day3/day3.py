def part1(): 
  score = 0
  with open("aoc22\day3\day3.txt", "r") as f:
    for i, val in enumerate(f.readlines()):
      val = val.rstrip()
      n = len(val)

      first, second = val[:n//2], val[n//2:]
      
      s_first, s_second = set(first), set(second)
      s = s_first.intersection(s_second)
      val = s.pop()

      score += ord(val) - ord('a') + 1 if val.islower() else ord(val.lower()) - ord('a') + 27

  print(score)
    

def part2():
  score = 0
  with open("aoc22\day3\day3.txt", "r") as f:
    content = list(map(lambda x: x.rstrip(), f.readlines()))
    for i in range(0, len(content), 3):
      set1, set2, set3 = set(content[i]), set(content[i+1]), set(content[i+2]), 
      s = set1.intersection(set2, set3)
      val = s.pop()

      score += ord(val) - ord('a') + 1 if val.islower() else ord(val.lower()) - ord('a') + 27
  
  print(score)

if __name__ == "__main__":
  part1()
  part2()