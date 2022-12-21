from collections import defaultdict
import re

def parse_string(string):
  arr = string.split(" ")
  return [arr[0]] + [arr[2]], arr[1]

def part1(string="root"):
  with open("aoc22/day21/day21.txt") as f:
    map = defaultdict(tuple)
    for _, line in enumerate(f.readlines()):
      name, job = line.rstrip().split(": ")
      if len(job) > 2: # not a number
        # parse and return the two operands and the operator
        operands,  operator = parse_string(job)
        map[name] = (operator, operands)
      else:
        map[name] = (None, int(job))

    def findRoot(name): 
      if map[name][0] == None:
        return map[name][1]

      elif map[name][0] == "+":
        return findRoot(map[name][1][0]) + findRoot(map[name][1][1])
      elif map[name][0] == "*":
        return findRoot(map[name][1][0]) * findRoot(map[name][1][1])
      elif map[name][0] == "-":
        return findRoot(map[name][1][0]) - findRoot(map[name][1][1])
      elif map[name][0] == "/":
        return findRoot(map[name][1][0]) / findRoot(map[name][1][1])
      else:
        raise Exception("Unknown operator")

    print(findRoot(string))

def part2():
  with open("aoc22/day21/day21.txt") as f:
    monkeys = {}
    for _, line in enumerate(f.readlines()):
      name, value = map(str.strip, line.split(':'))
      monkeys[name] = value if value[0].isdigit() else value.split()

      def unwind(name):
        monkey = monkeys[name]

        if isinstance(monkey, list):
            expr = unwind(monkey[0]), monkey[1], unwind(monkey[2])
            return "({0} {1} {2})".format(*expr)
          
        return monkey

  from sympy.solvers import solve

  monkeys['root'][1] = '-' # Will sove for expression equals 0
  monkeys['humn'] = 'x'

  print(solve(unwind('root'))[0])

if __name__ == "__main__":
  part1()
  part2()