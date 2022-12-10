def part1(): 
  with open("aoc22\day10\day10.txt", "r") as f:
    X = 1
    cycles = 0
    cycles_mappings = {}
    sum = 0
    # 20th, 60th, 100th, 140th, 180th, and 220th
    report = [20, 60, 100, 140, 180, 220]
    for _, val in enumerate(f.readlines()):
      val = val.rstrip()
      if val == "noop":
        cycles += 1
        cycles_mappings[cycles] = X
      else: 
        num = int(val.split(" ")[1])
        for i in range(2):
          cycles += 1
          cycles_mappings[cycles] = X

        X += num
    
    for i in report:
      sum += i * cycles_mappings[i] 

    print(sum)
    return cycles_mappings

  
def part2():
  cycle_mappings = part1()
  ans = [["." for _ in range(40)] for _ in range(6)] 
  for key, val in cycle_mappings.items():
    pos = (key - 1) % 40
    if pos in [val - 1, val, val + 1]:
      row = key // 40 
      ans[row][pos] = "#"
    
  ans = list(map(lambda x: "".join(x), ans))
  for i in ans:
    print(i)

if __name__ == "__main__":
  print(part1())
  print(part2())
