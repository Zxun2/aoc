def create_grid():
  grid = []
  with open("aoc22\day12\day12.txt") as file:
    for line in file.readlines():
      grid.append(list(line.strip()))

  start = None
  arrOfA = []
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "S":
        start = (i, j)
        grid[i][j] = "a"
      elif grid[i][j] == "a" :
        arrOfA.append((i, j))
      else:
        continue
  return grid, [start] + arrOfA 

def part1(grid, start):
  goal_state = "E"
  queue = [(start[0], start[1], 0, [])]
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  seen = set()
  seen.add(start)
  while queue: 
    y, x, steps, path = queue.pop(0)
    if grid[y][x] == goal_state:
      print(steps)
      return steps

    curr = grid[y][x]
    for y_, x_ in neighbors:
      if 0 <= y+y_ < len(grid) and 0 <= x+x_ < len(grid[0]):
        dest = grid[y+y_][x+x_] 
        if dest == goal_state:
          dest = "z"
        if dest != "#" and (ord(dest) - ord(curr)) < 2 and (y+y_, x+x_) not in seen:
          queue.append((y+y_, x+x_, steps+1, path + [grid[y+y_][x+x_]]))
          seen.add((y+y_, x+x_))

  print("no solution found")
  return float('inf')

def part2(grid, arr):
  minSteps = float('inf')
  for i, start in enumerate(arr): 
    steps = part1(grid, start)
    minSteps = min(minSteps, steps)

  print("minSteps: ", minSteps)
  return minSteps

if __name__ == "__main__":
  grid, arr = create_grid()
  part1(grid, arr[0])
  part2(grid, arr)