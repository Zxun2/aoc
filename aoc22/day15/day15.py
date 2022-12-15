import z3

sensors = {}
multiplier = 4000000

def part1(target=2000000):
  '''
  return beacons locations that are not possible
  '''
  global sensors 

  with open("aoc22/day15/day15.txt") as f:
    row = set()
    min_x = float('inf')
    max_x = float('-inf')
    for _, line in enumerate(f.readlines()):
      sensor, beacon = line.strip().split(":")
      sensor = tuple(map(lambda x: int(x[2:]), sensor.split(",")))
      beacon = tuple(map(lambda x: int(x[2:]), beacon.split(",")))
      dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) 
      min_x = min(min_x, sensor[0], beacon[0])
      max_x = max(max_x, sensor[0], beacon[0])

      sensors[sensor] = dist

      vert_distance = abs(target - sensor[1])
      if (hd := dist - vert_distance) >= 0:
        for i in range(-hd, hd+1):
          row.add((sensor[0] + i, target))

      if beacon in row:
        row.remove(beacon)

    print(len(row))
    
def part2():
  '''
  z3 saved my life, no cap.
  '''
  x = z3.Int("x")
  y = z3.Int("y")
  solver = z3.Solver()
  solver.add(x >= 0, x <= 4000000, y >= 0, y <= 4000000)
  with open("aoc22/day15/day15.txt") as f:
    for _, line in enumerate(f.readlines()):
      sensor, beacon = line.strip().split(":")
      sensor = tuple(map(lambda x: int(x[2:]), sensor.split(",")))
      beacon = tuple(map(lambda x: int(x[2:]), beacon.split(",")))
      manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) 
      solver.add(z3.Abs(sensor[1] - y) + z3.Abs(sensor[0] - x) > manhattan)
  solver.check()
  model = solver.model()
  print(model[x].as_long() * 4000000 + model[y].as_long())


if __name__ == "__main__":
  part1()
  part2()