def create_grid():
  with open("aoc22\day8\day8.txt", "r") as f:
    grid = []
    for _, val in enumerate(f.readlines()):
      val = val.strip()
      arr = []
      for i in val: 
        arr.append(int(i))
      grid.append(arr)
    return grid

def part1(): 
  grid = create_grid()
  m, n = len(grid), len(grid[0])
  ans = 2 * m + 2 * n - 4

  # code written by copilot 
  for i in range(1, m-1):
    for j in range(1, n-1):
      curr = grid[i][j]
      # check left 
      if max(grid[i][:j]) < curr:
        ans += 1
        continue
      # check right
      if max(grid[i][j+1:]) < curr:
        ans += 1
        continue   
      # check up
      if max([grid[k][j] for k in range(i)]) < curr:
        ans += 1
        continue
      # check down    
      if max([grid[k][j] if k < m else 0 for k in range(i+1, m)]) < curr:    
          ans += 1
          continue

  return ans

def part2():
  grid = create_grid()
  m, n = len(grid), len(grid[0])
  score = -float('inf')
  
  for i in range(m):
    for j in range(n):
      curr = grid[i][j]
      c_score = 1 
      l, r, u, d = 0, 0, 0, 0

      # check left 
      for k in range(j-1, -1, -1):
        if grid[i][k] < curr:
          l += 1
        else:
          l += 1
          break
        
      # check right
      for k in range(j+1, n):
        if grid[i][k] < curr:
          r += 1
        else:  
          r += 1
          break
      
      # check up
      for k in range(i-1, -1, -1):
        if grid[k][j] < curr:
          u += 1
        else:
          u += 1
          break

      # check down
      for k in range(i+1, m): 
        if grid[k][j] < curr:
          d += 1
        else:
          d += 1
          break
      
      c_score *= l * r * u * d
      score = max(score, c_score)

  return score

if __name__ == "__main__":
  print(part1())
  print(part2())
