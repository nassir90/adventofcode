from starter import get_puzzle_input
import pdb

small_plot = [ [ int(char) for char in line ] for line in get_puzzle_input(15, False) ]
plot = [ [ 0 for x in range(len(small_plot[0])* 5) ] for y in range(len(small_plot) * 5) ]
interval = len(small_plot)

for y in range(len(plot)):
    for x in range(len(plot[0])):
        to_add = y // interval + x // interval
        value = small_plot[y % interval][x % interval] + to_add
        if value > 9:
            value -= 9
        #print(value, end=" ")
        plot[y][x] = value
    #print()

def get_neighbors(y, x):
    neighbors = []
    if y != 0:
        neighbors.append((y - 1, x))
    if x != len(plot[0]) - 1:
        neighbors.append((y, x + 1))
    if y != len(plot) - 1:
        neighbors.append((y + 1, x))
    if x != 0:
        neighbors.append((y,x-1))
    return neighbors

def get_offset(y, x):
    return y // interval + x // interval

# Using djikstra feels cheap but it is what it is.
# At least I understand how it works now.
def find_shortest(sy, sx, dy, dx):
    current_risk_levels = [ [ float("inf") for x in row ] for row in plot ]
    current_risk_levels[sy][sx] = 0
    border = get_neighbors(sy, sx)
    visited = [ [ False for x in row ] for row in plot ]
    while not visited[dy][dx]:
        minimum_point = border[0]
        for y, x in border[1:]:
            if current_risk_levels[y][x] < current_risk_levels[minimum_point[0]][minimum_point[1]]:
                minimum_point = (y, x)
        my, mx = minimum_point
        for ny, nx in get_neighbors(my, mx):
            if not visited[ny][nx]:
                border.append((ny, nx))
                potential_risk = current_risk_levels[my][mx] + plot[ny][nx]
                if potential_risk < current_risk_levels[ny][nx]:
                    current_risk_levels[ny][nx] = potential_risk
                visited[ny][nx] = True
        border.remove(minimum_point)
    print(current_risk_levels[-1][-1]) 

find_shortest(10,10, -1, -1)
