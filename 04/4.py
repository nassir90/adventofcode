import pdb
import sys

file = open(sys.argv[1])
numbers = [int(number) for number in next(file).split(",")]

boards = [] 

board_row = 0
current_board = 0

for line in file:
    line = line.strip()
    if line:
        boards[current_board].append({ int(number) : False for number in line.split() })
        board_row += 1
        if board_row == 5:
            board_row = 0
            current_board += 1
    else:
        boards.append([])

def board_has_won(board):
    syboard = board
    lmaoboard = [list(row.values()) for row in board]
    won = False
    for row in lmaoboard:
        if len([a for a in row if a]) == 5:
            won = True
    for x in range(5):
        if len([lmaoboard[y][x] for y in range(5) if lmaoboard[y][x]]) == 5:
            won = True
    sum_ = 0
    for row in syboard:
        for key in row:
            if not row[key]:
                sum_ += key
    if won:
        print(sum_)
    return won, sum_

boards_that_have_won = []
last_board_to_win = None

for number in numbers:
    for index, board in enumerate(boards):
        for row in board:
            if row.get(number) is not None:
                row[number] = True
        if index not in boards_that_have_won:
            won, score = board_has_won(board)
            if won:
                boards_that_have_won.append(index)
                last_board_to_win = (index, score, number)

index, score, number = last_board_to_win
print("Board %d will win with score %d " % (index + 1, score * number))
