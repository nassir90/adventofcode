from starter import get_puzzle_input

heigtmap = [ [ int(char) for char in line.strip() ] for line in get_puzzle_input(9) ]

low_points = []

for y in range(len(heigtmap)):
    for x in range(len(heigtmap[0])):
        if y != 0 and heigtmap[y-1][x] > heigtmap[y][x] \
        or x != len(heigtmap[0]) - 1 and heigtmap[y][x+1] > heigtmap[y][x] \
        or x != 0 and heigtmap[y][x-1] > heigtmap[y][x] \
        or y != len(heigtmap) - 1 and heigtmap[y+1][x] > heigtmap[y][x]:
            low_points.append((y,x))

def get_basin_size(start, checked):
    checked.append(start)
    y, x = start
    size = 1
    for y2, x2 in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if y2 != -1 and x2 != -1 \
        and y2 != len(heigtmap) and x2 != len(heigtmap[0]) \
        and (y2, x2) not in checked \
        and heigtmap[y2][x2] > heigtmap[y][x] \
        and heigtmap[y2][x2] != 9:
            size += get_basin_size((y2,x2), checked)
    return size

basin_sizes = [];

for low_point in low_points:
    basin_sizes.append(get_basin_size(low_point, []))

basin_sizes.sort()
result = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
print(result)
