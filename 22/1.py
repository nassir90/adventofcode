from starter import get_puzzle_input
import pdb

commands = []
for line in get_puzzle_input(22, False):
    command, cuboid = line.split()
    coordinates = cuboid.split(",")
    ranges = []
    for coordinate in coordinates:
        ranges.append([int(point) for point in coordinate[2:].split("..")])
    commands.append([command, ranges])

on = [ [ [False for z in range(-50,51) ] for y in range(-50, 51) ] for x in range(-50, 51) ]

for command, (xrange, yrange, zrange) in commands:
    if xrange[0] >= -50 and xrange[1] <= 50:
        for x in range(xrange[0], xrange[1]+1):
            if yrange[0] >= -50 and yrange[1] <= 50:
                for y in range(yrange[0], yrange[1]+1):
                    if zrange[0] >= -50 and zrange[1] <= 50:
                        for z in range(zrange[0], zrange[1]+1):
                            if command == "on":
                                on[x][y][z] = True
                            else:
                                on[x][y][z] = False

on_ = 0

for x in on:
    for y in x:
        for z in y:
            if z:
                on_ += 1

print(on_)
