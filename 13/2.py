from starter import get_puzzle_input
import pdb

lines = get_puzzle_input(13, False)
split = lines.index('')
head, tail = [ tuple(map(int, c.split(','))) for c in lines[:split]], lines[split+1:]
print(head[-1])
maximum_x = max(point[0] for point in head)
maximum_y = max(point[1] for point in head)
plot = [ [ '#' if (x,y) in head else '.' for y in range(maximum_y + 1) ] for x in range(maximum_x + 1) ]

for instruction in tail:
    instruction = instruction.split('=')
    fold_along = int(instruction[1])
    if instruction[0] == 'fold along y':
        above = [ [ char for y, char in enumerate(x) if y < fold_along] for x in plot]
        below_flipped = [ [ char for y, char in enumerate (x) if y > fold_along]  for x in plot]
        for l in below_flipped:
            l.reverse()
        print("dong")
        for y, row in enumerate(below_flipped):
            for x, value in enumerate(row):
                if value == '#':
                    above[y][x] = value
        for line in above:
            for char in line:
                print(char, end="")
            print()
        plot = above
    else:
        left = [ [ value for value in row ] for x, row in enumerate(plot) if x < fold_along ]
        right = [ [ value for value in row ] for x, row in enumerate(plot) if x > fold_along ]
        right.reverse()
        print("long")
        for y, row in enumerate(right):
            for x, value in enumerate(row):
                if value == '#':
                    left[y][x] = value
        for line in left:
            for char in line:
                print(char, end="")
            print()
        plot = left
