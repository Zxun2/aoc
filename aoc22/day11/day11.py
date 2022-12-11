from typing import Callable, List

class Monkey:
  def __init__(self, monkey: int, curr_items: List[int], update: Callable[[int], int], condition: Callable[[int], bool]):
    self.monkey = monkey
    self.curr_items = curr_items
    self.update = update
    self.condition = condition
    self.inspectCount = 0
    self.modulo = 9699690

  def throw(self, new_item: int): 
    if self.condition(new_item):
      self.t._addItem(new_item)
    else:
      self.f._addItem(new_item)

  def inspect(self):
    while self.curr_items:
      item = self.curr_items.pop(0)
      new_worry = self.update(item) % self.modulo
      self.throw(new_worry) # throw to next monkey
      self.inspectCount += 1

  def _addItem(self, item: int):
    self.curr_items.append(item)

  def setNextTrue(self, t: "Monkey", f: "Monkey"):
    self.t = t
    self.f = f

# init monkeys
mon0 = Monkey(0, [93, 54, 69, 66, 71], lambda x: x * 3, lambda y: y % 7 == 0)
mon1 = Monkey(1, [89, 51, 80, 66], lambda x: x * 17, lambda y: y % 19 == 0)
mon2 = Monkey(2, [90, 92, 63, 91, 96, 63, 64], lambda x: x + 1, lambda y: y % 13 == 0)
mon3 = Monkey(3, [65, 77], lambda x: x + 2, lambda y: y % 3 == 0)
mon4 = Monkey(4, [76, 68, 94], lambda x: x ** 2, lambda y: y % 2 == 0)
mon5 = Monkey(5, [86, 65, 66, 97, 73, 83], lambda x: x + 8, lambda y: y % 11 == 0)
mon6 = Monkey(6, [78], lambda x: x + 6, lambda y: y % 17 == 0)
mon7 = Monkey(7, [89, 57, 59, 61, 87, 55, 55, 88], lambda x: x + 7, lambda y: y % 5 == 0)
print("Successfully initialized monkeys")


# set links
mon0.setNextTrue(mon7, mon1)
mon1.setNextTrue(mon5, mon7)
mon2.setNextTrue(mon4, mon3)
mon3.setNextTrue(mon4, mon6)
mon4.setNextTrue(mon0, mon6)
mon5.setNextTrue(mon2, mon3)
mon6.setNextTrue(mon0, mon1)
mon7.setNextTrue(mon2, mon5)
print("Successfully set links")

def part1():
  for _ in range(20):
    for m in [mon0, mon1, mon2, mon3, mon4, mon5, mon6, mon7]:
      m.inspect()
  
  ans = []
  for m in [mon0, mon1, mon2, mon3, mon4, mon5, mon6, mon7]:
    ans.append(m.inspectCount)

  ans = sorted(ans)
  print(ans[-1] * ans[-2])


def part2():
  for i in range(10000):
    for m in [mon0, mon1, mon2, mon3, mon4, mon5, mon6, mon7]:
      m.inspect()
  
  ans = []
  for m in [mon0, mon1, mon2, mon3, mon4, mon5, mon6, mon7]:
    ans.append(m.inspectCount)

  ans = sorted(ans)
  print(ans[-1] * ans[-2])

if __name__ == "__main__":
  part1()
  part2()