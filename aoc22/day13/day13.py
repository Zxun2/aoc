import pathlib
from functools import cmp_to_key
from typing import Union

Packet = Union[int, list['Packet']]
def read_packets(file: pathlib.Path) -> list[list[Packet]]:
  with open(file) as f:
    packets = [eval(output) for output in (line.strip() for line in f) if len(output)]
  return packets

def cmp(left, right):
  for i in range(min(len(left), len(right))):
      if type(left[i]) == int and type(right[i]) == int:
          if left[i] == right[i]:
              continue
          return left[i] - right[i]
      ret = cmp(
          left[i] if isinstance(left[i], list) else [left[i]],
          right[i] if isinstance(right[i], list) else [right[i]]
      )
      if ret:
          return ret
  return len(left) - len(right)

if __name__ == "__main__":
  packets = read_packets(pathlib.Path(__file__).parent / 'day13.txt')
  indices1 = sum(i // 2 + 1 for i in range(0, len(packets), 2) if cmp(*packets[i:i + 2]) < 0)
  packets += [[[2]], [[6]]]
  packets = sorted(packets, key=cmp_to_key(cmp))
  indices2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
  print(indices1)
  print(indices2)