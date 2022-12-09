def part1(): 
  with open("aoc22\day9\day9.txt", "r") as f:
    visited = set()
    tail, head = (0, 0), (0, 0) # (c, r)
    visited.add(tail) # add starting position
    directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
    for _, val in enumerate(f.readlines()):
      val = val.strip()
      # distance head will move
      dir, steps = val.split(' ')
      steps = int(steps)

      # update head
      for _ in range(steps):
        head = (head[0] + directions[dir][0], head[1] + directions[dir][1])
        tail = getTail(head, tail)
        visited.add(tail)

    return len(visited) 

def part2():
   with open("aoc22\day9\day9.txt", "r") as f:
    visited = set()
    tails, head = [(0, 0) for _ in range(9)], (0, 0) # (c, r)
    visited.add(head) # add starting position
    directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
    for _, val in enumerate(f.readlines()):
      val = val.strip()
      # distance head will move
      dir, steps = val.split(' ')
      steps = int(steps)

      # update head
      for _ in range(steps):
        head = (head[0] + directions[dir][0], head[1] + directions[dir][1])
        tmp = head
        for i in range(9):
          tails[i] = getTail(tmp, tails[i])
          tmp = tails[i]

        visited.add(tails[-1])

    return len(visited) 

def getTail(head, tail):
  # if either c or r is the same, we can just iterate through the range
  if (head[0] == tail[0]) :  # same cols
    start = min(head[1], tail[1])
    end = max(head[1], tail[1])
    for _ in range(start + 1, end):
      addRow = 1 if head[1] > tail[1] else -1
      tail = (tail[0], tail[1] + addRow) 
  elif (head[1] == tail[1]): # same rows
    start = min(head[0], tail[0]) 
    end = max(head[0], tail[0]) 
    for _ in range(start + 1, end):
      addCol = 1 if head[0] > tail[0] else -1
      tail = (tail[0] + addCol, tail[1]) 
  elif abs(head[0] - tail[0]) >= 2: # not the same row and number of cols differ by more than 2
    # make a diagonal move in the direction of head
    tail = (tail[0] + (1 if head[0] > tail[0] else -1), tail[1] + (1 if head[1] > tail[1] else -1))
    for _ in range(min(tail[0], head[0]) + 1, max(head[0], tail[0])):
      tail = (tail[0] + (1 if head[0] > tail[0] else -1), tail[1]) # same row
  elif abs(head[1] - tail[1]) >= 2: # not the same col and number of rows differ by more than 2
    # make a diagonal move in the direction of head
    tail = (tail[0] + (1 if head[0] > tail[0] else -1), tail[1] + (1 if head[1] > tail[1] else -1))
    for _ in range(min(tail[1], head[1]) + 1, max(head[1], tail[1])):
      tail = (tail[0], tail[1] + (1 if head[1] > tail[1] else -1)) # same col
  else: # not the same row or col and number of cols or rows differ by 1
    pass # do nothing
  return tail

if __name__ == "__main__":
  print(part1())
  print(part2())
