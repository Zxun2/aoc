from collections import defaultdict

def build_stacks():
  stack_dict = defaultdict(list)
  stack_dict[1].extend(["S", "L", "W"])
  stack_dict[2].extend(["J", "T", "N", "Q"])
  stack_dict[3].extend(["S", "C", "H", "F", "J"])
  stack_dict[4].extend(["T", "R", "M", "W", "N", "G", "B"])
  stack_dict[5].extend(["T", "R", "L", "S", "D", "H", "Q", "B"])
  stack_dict[6].extend(["M", "J", "B", "V", "F", "H", "R", "L"])
  stack_dict[7].extend(["D", "W", "R", "N", "J", "M"])
  stack_dict[8].extend(["B", "Z", "T", "F", "H", "N", "D", "J"])
  stack_dict[9].extend(["H", "L", "Q", "N", "B", "F", "T"])
  return stack_dict

def part1(): 
  cargo = build_stacks()
  with open("aoc22\day5\day5.txt", "r") as f:
    for i, val in enumerate(f.readlines()):
      val = val.rstrip()
      val = val.split(" ")
      numMove = int(val[1])
      from_ = int(val[3])
      to_ = int(val[5])

      for _ in range(numMove):
        c = cargo[from_].pop()
        cargo[to_].append(c)
      
  print("".join(list(map(lambda x: x[-1], cargo.values()))))

def part2():
  cargo = build_stacks()
  with open("aoc22\day5\day5.txt", "r") as f:
    for i, val in enumerate(f.readlines()):
      val = val.rstrip()
      val = val.split(" ")
      numMove = int(val[1])
      from_ = int(val[3])
      to_ = int(val[5])

      tmp = cargo[from_][-numMove:]
      for _ in range(numMove):
        cargo[from_].pop()
      
      cargo[to_].extend(tmp)
      
  print("".join(list(map(lambda x: x[-1], cargo.values()))))
  
  return

if __name__ == "__main__":
  part1()
  part2()