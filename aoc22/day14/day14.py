def create_grid(extend=False): 
  with open("aoc22/day14/day14.txt") as f:
    lines = f.readlines()
    lines = [line.strip().split(" -> ") for line in lines]
    lines = [list(map(lambda x: tuple(list(map(lambda y: int(y), x.split(",")))), line)) for line in lines]
    
    min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')

    for line in lines:
      for x, y in line: 
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    min_y = min(min_y, 0)
    max_y = max(max_y, 0) if not extend else max(max_y, 0) + 2
    min_x = min(min_x, 500) if not extend else min(min_x, 500) - (max_y - min_y)
    max_x = max(max_x, 500) if not extend else max(max_x, 500) + (max_y - min_y)
    
    # create grid 
    grid = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for line in lines:
      for i, (x, y) in enumerate(line):
        if i == len(line) - 1:
          continue 
        start_y = y - min_y
        end_y = line[i+1][1] - min_y
        start_x = x - min_x
        end_x = line[i+1][0] - min_x

        for j in range(min(start_y, end_y), max(start_y, end_y) + 1):
          for k in range(min(start_x, end_x), max(start_x, end_x) + 1):
            grid[j][k] = "#"

    grid[0][500 - min_x] = "+"
    for i in range(len(grid[0])):
      grid[max_y][i] = "#"

    return grid, min_x, max_x, min_y, max_y

def display_grid(grid):
  for row in grid:
    print(row)
    
  print("\n")

def part1():
  grid, min_x, max_x, min_y, max_y = create_grid()
  n_cols, n_rows = len(grid[0]), len(grid)
  num = 0
  while True:
    prev_pos = (500 - min_x, -1)
    curr_pos = (500 - min_x, 0)
    while prev_pos != curr_pos:
      # waterfall
      new_y = curr_pos[1] + 1
      new_x = curr_pos[0]

      if new_y >= n_rows or new_x < 0 or new_x >= n_cols: 
        print(num)
        return 

      if grid[new_y][new_x] == ".":
        prev_pos = curr_pos
        curr_pos = (new_x, new_y)
      else:
        if new_y >= n_rows or new_x - 1 < 0 or new_x + 1 >= n_cols: 
          print(num)
          return 

        # check left and right
        if grid[new_y][new_x - 1] == ".":
          prev_pos = curr_pos
          curr_pos = (new_x - 1, new_y)
        elif grid[new_y][new_x + 1] == ".":
          prev_pos = curr_pos
          curr_pos = (new_x + 1, new_y)
        else: 
          prev_pos = curr_pos
    
    if curr_pos[1] >= n_rows or curr_pos[0] < 0 or curr_pos[0] >= n_cols:
      break

    num += 1
    grid[curr_pos[1]][curr_pos[0]] = "o"

def part2():
  grid, min_x, max_x, min_y, max_y = create_grid(True)
  n_cols, n_rows = len(grid[0]), len(grid)
  num = 0
  while True:
    prev_pos = (500 - min_x, -1)
    curr_pos = (500 - min_x, 0)
    if grid[curr_pos[1]][curr_pos[0]] == "o":
      print(num)
      return

    while prev_pos != curr_pos:
      # waterfall
      new_y = curr_pos[1] + 1
      new_x = curr_pos[0]

      if new_y >= n_rows or new_x < 0 or new_x >= n_cols: 
        print(num)
        return 

      if grid[new_y][new_x] == ".":
        prev_pos = curr_pos
        curr_pos = (new_x, new_y)
      else:
        if new_y >= n_rows or new_x - 1 < 0 or new_x + 1 >= n_cols: 
          print(num)
          return 

        # check left and right
        if grid[new_y][new_x - 1] == ".":
          prev_pos = curr_pos
          curr_pos = (new_x - 1, new_y)
        elif grid[new_y][new_x + 1] == ".":
          prev_pos = curr_pos
          curr_pos = (new_x + 1, new_y)
        else: 
          prev_pos = curr_pos
    
    num += 1
    grid[curr_pos[1]][curr_pos[0]] = "o"
  
if __name__ == "__main__":
  part1()
  part2()