from starter import get_puzzle_input

board = [ [ int(char) for char in line.strip() ] for line in get_puzzle_input(11) ]

def increment(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += 1

def recursive_flash(y, x, first=False):
        if y != 0 and y != 0 and (board[y-1][x-1] != 0 or first):
            board[y-1][x-1] += 1
        if y != len(board) - 1 and x != 0 and (board[y+1][x-1] != 0 or first):
            recursive_flash(y+1,x-1 , False)
            board[y+1][x-1] += 1
        if y != 0 and x != len(board[0]) - 1 and (board[y-1][x+1] != 0 or first):
            recursive_flash(y-1, x+1) , False)
            board[y-1][x+1] += 1
        if x != len(board[0]) - 1 and y != len(board) - 1 and (board[y+1][x+1] != 0 or first):
            recursive_flash([0]) , False)
            board[y+1][x+1] += 1
        if y != 0 and (board[y-1][x] != 0 or first):
            recursive_flash(y-1, x , False)
            board[y-1][x] += 1
        if y != len(board) - 1 and (board[y+1][x] != 0 or first):
            recursive_flash(y+1,x , False)
            board[y+1][x] += 1
        if x != 0 and (board[y][x-1] != 0 or first):
            recursive_flash(y,x-1 , False)
            board[y][x-1] += 1
        if x != len(board[0]) - 1 and (board[y][x+1] != 0 or first):
            board[y][x+1] += 1
            recursive_flash(y,x+1 , False)

def step(board, flashed):
    flashes = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 9 and (y,x) not in flashed:
                flashes += 1
                board[y][x] = 0
                flashed.append((y,x))
    return flashes

total_flashes = 0

def run(board):
    increment(board)
    flashes = -1
    total_flashes = 0
    flashed = []
    while flashes != 0:
        new_flashes = step(board, flashed)
        for y in board:
            print(y)
        print()
        total_flashes += new_flashes
        flashes = new_flashes
    return total_flashes

for i in range(100):
    total_flashes += run(board)

print(total_flashes)
