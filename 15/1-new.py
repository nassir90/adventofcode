from starter import get_puzzle_input
import pdb

plot = [ [ int(char) for char in line ] for line in get_puzzle_input(15, False) ]

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

def find_shortest():
    unvisited = [ (y, x) for x in range(len(plot[0])) for y in range(len(plot)) ]
    current_risk_levels = [ [ float("Infinity") for x in row ] for row in plot ]
    current_risk_levels[0][0] = 0

    while len(unvisited) != 0:
        minimum_point = unvisited[0]
        for y, x in unvisited:
            if current_risk_levels[y][x] < current_risk_levels[minimum_point[0]][minimum_point[1]]:
                minimum_point = (y, x)
        my, mx = minimum_point
        for ny, nx in get_neighbors(my, mx):
            potential_risk = current_risk_levels[my][mx] + plot[ny][nx]
            if potential_risk < current_risk_levels[ny][nx]:
                current_risk_levels[ny][nx] = potential_risk
        unvisited.remove(minimum_point)
    print(current_risk_levels[-1][-1]) 

find_shortest()
