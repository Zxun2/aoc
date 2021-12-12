# arr = [5,3,8,4,2,7,1,10]

# def partition(arr, low, high):
 
#     pivot = arr[low]
#     i = low -1 
#     j = high +1
 
#     while (True):
 
#         # Find leftmost element greater than
#         # or equal to pivot
#         print(i, 0)
#         i += 1
#         while (arr[i] < pivot):
#             i += 1
#         print(i)
#         # Find rightmost element smaller than
#         # or equal to pivot
#         print(j, 1)
#         j -= 1
#         while (arr[j] > pivot):
#             j -= 1
#         print(j)
#         # If two pointers met.
#         if (i >= j):
#             return j
 
#         arr[i], arr[j] = arr[j], arr[i]
    

# print(partition(arr, 0, len(arr)-1))

import collections

file1 = open('day4.txt', 'r')
lines = list(map(lambda x: x.rstrip(), file1.readlines()))
randomNumbers = lines[0].split(',')
BigBoard = collections.defaultdict(list) 
BoardNum = 0
winningBoard = None
numBoards_won = []
for string in lines[2: ]:
    if string == '':
        BoardNum += 1
    else: 
        nums = string.split()

        Board = BigBoard[BoardNum]
        Board.append(nums)


def checkWin(board):
    rows = len(board)
    cols = len(board[0])

    winning_row = ["*" for i in range(cols)]
    if winning_row in board:
        return True
    else: 
        #check cols
        win = False 
        for i in range(cols):
            temp = True
            for j in range(rows):
                temp = temp and board[j][i] == "*" 
            win = temp or win

        return win

def checkScore(board):
    rows = len(board)
    cols = len(board[0])
    sum = 0
    for i in range(rows):
        for j in range(cols):
           if board[i][j] != "*":
               sum += int(board[i][j]) 

    return sum

def solve():
    for num in randomNumbers:
        for boardNum, board in BigBoard.items():
            for row in board:
                if num in row:
                    index = row.index(num)
                    row[index] = "*"  #mark
                    break
            
            # check for victory
            if checkWin(board):
                winningBoard = boardNum
                if winningBoard not in numBoards_won:
                    numBoards_won.append(winningBoard)
                
                if len(numBoards_won) == len(BigBoard):
                    print(BigBoard[numBoards_won[-1]])
                    score = checkScore(BigBoard[winningBoard])
                    return int(num) * score
solve()