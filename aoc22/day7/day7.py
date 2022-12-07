from bisect import bisect_left

class FileSystem:
  def __init__(self, curr_dir, size, parent):
    self.curr_dir = curr_dir
    self.size = size
    self.parent = parent

class File(FileSystem):
  def __init__(self, curr_dir, size, name, parent):
    super().__init__(curr_dir, size, parent)
    self.name = name

class Folder(FileSystem):
  def __init__(self, curr_dir, size, parent):
    super().__init__(curr_dir, size, parent)
    self.children = {}

def create_filesystem():
  with open("aoc22\day7\day7.txt", "r") as f:
    # initialize empty directory
    root = Folder("/", 0, None)
    curr = root
    for _, val in enumerate(f.readlines()):
      val = val.rstrip()
      io = val.split(" ")

      if io[0] == "$": # command
        if io[1] == "cd":
          if (to_dir := io[2]) == "/":
            curr = root
          elif to_dir == "..":
            if curr.curr_dir != "/":
              curr = curr.parent
          else:
            if to_dir not in curr.children:
              curr.children[to_dir] = Folder(to_dir, 0, curr)
            curr = curr.children[to_dir]
      else: # not a command
        if io[0] == "dir": 
          folder = io[1]
          if folder not in curr.children:
            curr.children[folder] = Folder(folder, 0, curr)
        else: # a normal file
          size = int(io[0])
          filename = io[1]
          if filename not in curr.children:
            curr.children[filename] = File(curr.curr_dir, size, filename, curr)
    return root

def part1(): 
  MAX_SIZE = 100000
  root = create_filesystem()
  total_size = 0

  def findSize(node):
    nonlocal total_size

    if isinstance(node, File):  
      return node.size

    node.size = sum(list(map(lambda n: findSize(n), node.children.values())))

    if node.size <= MAX_SIZE:
      total_size += node.size

    return node.size

  findSize(root)
  return total_size, root

def part2():
  _, root = part1()
  TOTAL_SIZE = 70000000
  REQUIRED_SPACE = 30000000 
  TARGET_SIZE = root.size - TOTAL_SIZE + REQUIRED_SPACE
  arr = []
  def contiguous_arr(node):
    nonlocal arr
    if isinstance(node, File):
      return
    arr.append(node.size)
    for node in node.children.values():
      contiguous_arr(node)

  contiguous_arr(root)
  arr = sorted(arr)
  return arr[bisect_left(arr, TARGET_SIZE)]

if __name__ == "__main__":
  print(part1())
  print(part2())