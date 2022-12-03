def part1(): 
  move_scores = {"X": 1, "Y": 2, "Z": 3}
  move_wins = {"A": ("Z", "X"), "B": ("X", "Y"), "C": ("Y", "Z")}
  score = 0

  with open("aoc22\day2\day2.txt", "r") as f:
    for i, val in enumerate(f.readlines()):
      opp, move = val.rstrip().split(" ")
      if move not in move_wins[opp]:
        score += 6 # win
      elif move == move_wins[opp][1]:
        score += 3 # draw

      score += move_scores[move]

  print(score)


def part2():
  win_scores = {"X": 0, "Y": 3, "Z": 6}
  move_scores = {"A": 1, "B": 2, "C": 3}
  move_wins = {"A": ("C", "B"), "B": ("A", "C"), "C": ("B", "A")}
  score = 0

  with open("aoc22\day2\day2.txt", "r") as f:
    for i, val in enumerate(f.readlines()):
      opp, outcome = val.rstrip().split(" ")
      
      if outcome == "X": # lose
        score += move_scores[move_wins[opp][0]]
      elif outcome == "Y": # draw
        score += move_scores[opp]
      else: # win
        score += move_scores[move_wins[opp][1]]

      score += win_scores[outcome]

  print(score)

if __name__ == "__main__":
  part1()
  part2()