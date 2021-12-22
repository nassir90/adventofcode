from starter import get_puzzle_input
import copy
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
first_non_init = 0

area = 0

ranges = []

def point_in_range(point, r):
#    print(point)
#    print(r)
    (xmin, xmax), (ymin, ymax), (zmin, zmax) = r
    x, y, z = point
    return x >= xmin and x < xmax and \
        y >= ymin and y < ymax and \
        z >= zmin and z < zmax


def clamp(number, minimum, maximum):
    return max(minimum, min(number, maximum))

def determine_point_overlaps_of(obj, subject):
    (xmin1, xmax1), (ymin1, ymax1), (zmin1, zmax1) = obj
    (xmin2, xmax2), (ymin2, ymax2), (zmin2, zmax2) = subject
    xmin1 = clamp(xmin1, xmin2, xmax2-1)
    xmax1 = clamp(xmax1, xmin2, xmax2-1)
    ymin1 = clamp(ymin1, ymin2, ymax2-1)
    ymax1 = clamp(ymax1, ymin2, ymax2-1)
    zmin1 = clamp(zmin1, zmin2, zmax2-1)
    zmax1 = clamp(zmax1, zmin2, zmax2-1)
    overlaps = []
    points = [
        (xmin1, ymin1, zmin1),
        (xmin1, ymin1, zmax1),
        (xmin1, ymax1, zmin1),
        (xmin1, ymax1, zmax1),
        (xmax1, ymin1, zmin1),
        (xmax1, ymin1, zmax1),
        (xmax1, ymax1, zmin1),
        (xmax1, ymax1, zmax1)
    ]
    for point in points:
        if point_in_range(point, subject):
            overlaps += [point]
    print(len(overlaps))
    return overlaps

def get_area(r):
    return abs((r[0][1] - r[0][0]) * (r[1][1] - r[1][0]) * (r[2][1] - r[2][0]))

# In order to add a range, check for overlaps, delete any overlaps (union) and then simply add the range to the ranges array
def delete(r):
    new_ranges = []
    (xmin, xmax), (ymin, ymax), (zmin, zmax) = r
    for r2 in ranges:
        (xmin2, xmax2), (ymin2, ymax2), (zmin2, zmax2) = r2
        overlaps = determine_point_overlaps_of(r, r2)
        if len(overlaps) == 8:
            new_ranges.append(r2)
    return [ r for r in new_ranges if get_area(r) != 0 ]

def add(r):
    new_ranges = delete(r)
    new_ranges.append(r)
    return new_ranges

def calculate_area():
    area = 0
    for (lx, hx), (ly, hy), (lz, hz) in ranges:
        area += abs((hx - lx) * ( hy - ly) * (hz - lz))
    return area

for command in commands:
    if command[0] == "on":
        ranges = add(command[1])
    elif command[0] == "off":
        ranges = delete(command[1])
    for r in ranges:
        print(r)
    print("Area is now:", calculate_area())

# Do final block
