from starter import get_puzzle_input

heigtmap = [ list(map(int,iter(line.strip()))) for line in get_puzzle_input(9) ]

low_points = []

for y in range(len(heigtmap)):
    for x in range(len(heigtmap[0])):
        try:
            if y != 0:
                if heigtmap[y-1][x] <= heigtmap[y][x]:
                    continue
        except IndexError:
            pass
        try:
            if heigtmap[y][x+1] <= heigtmap[y][x]:
                continue
        except IndexError:
            pass
        try:
            if x != 0:
                if heigtmap[y][x-1] <= heigtmap[y][x]:
                    continue
        except IndexError:
            pass
        try:
            if heigtmap[y+1][x] <= heigtmap[y][x]:
                continue
        except IndexError:
            pass
        low_points.append((y,x))

def get_basin_size(start, checked):
    y, x = start
    checked.append((y,x))
    new_points = [(y1,x1) for y1, x1 in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)] if (y1,x1) not in checked and y1 != -1 and x1 != -1]
    size = 0
    for y2, x2 in new_points:
        try:
            if (y2, x2) not in checked and heigtmap[y2][x2] > heigtmap[y][x] and heigtmap[y2][x2] != 9:
                print("> " + str(y2) + "," + str(x2) + "=" + str(heigtmap[y2][x2]))
                size += 1 + get_basin_size((y2,x2), checked)
        except IndexError:
            pass
    return size

basin_sizes = [];

for low_point in low_points:
    checked = []
    print(low_point)
    size = get_basin_size(low_point, checked)
    basin_sizes.append(size + 1)

basin_sizes.sort()
lol = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
print(lol)
