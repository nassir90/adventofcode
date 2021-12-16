from starter import get_puzzle_input
import pdb

small_plot = [ [ int(char) for char in line ] for line in get_puzzle_input(15, False) ]
plot = [ [ 0 for x in range(len(small_plot[0])* 5) ] for y in range(len(small_plot) * 5) ]
interval = len(small_plot)

for y in range(len(plot)):
    for x in range(len(plot[0])):
        to_add = y // interval + x // interval
        value = small_plot[y % interval][x % interval] + to_add
        if value > 9: value -= 9
        #print(value, end=" ")
        plot[y][x] = value
    #print()

def get_neighbors(y, x):
    if y != 0:
        yield (y - 1, x)
    if x != len(plot[0]) - 1:
        yield (y, x + 1)
    if y != len(plot) - 1:
        yield (y + 1, x)
    if x != 0:
        yield (y, x-1)

def get_offset(y, x):
    if y < 0:
        y += len(plot)
    if x < 0:
        x += len(plot)
    return y // interval + x // interval

# Using djikstra feels cheap but it is what it is.
# At least I understand how it works now.
def find_shortest(sy, sx, dy, dx):
    current_risk_levels = [ [ [ float("inf") for x in row ] for row in plot ] for i in range(9)]
    current_risk_levels[get_offset(sy,sx)][sy][sx] = 0
    border = [(sy, sx)]
    visited = [ [ [ False for x in row ] for row in plot ] for i in range(9)]
    while not visited[get_offset(dy,dx)][dy % interval][dx % interval]:
        minimum_point = border[0]
        for y, x in border[1:]:
            if current_risk_levels[get_offset(y,x)][y % interval][x % interval] \
                    < current_risk_levels[get_offset(minimum_point[0], minimum_point[1])][minimum_point[0] % interval][minimum_point[1] % interval]:
                minimum_point = (y, x)
        my, mx = minimum_point
        for ny, nx in get_neighbors(my, mx):
            if not visited[get_offset(ny,nx)][ny % interval][nx % interval]:
                border.append((ny, nx))
                potential_risk = current_risk_levels[get_offset(my,mx)][my % interval][mx % interval] + plot[ny][nx]
                if potential_risk < current_risk_levels[get_offset(ny,nx)][ny % interval][nx % interval]:
                    current_risk_levels[get_offset(ny,nx)][ny % interval][nx % interval] = potential_risk
                visited[get_offset(ny, nx)][ny % interval][nx % interval] = True
        border.remove(minimum_point)
    return current_risk_levels[get_offset(dy,dx)][dy % interval][dx % interval]

print(find_shortest(0,0, -1, -1))
