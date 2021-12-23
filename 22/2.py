from starter import get_puzzle_input
import copy
import pdb

commands = []
for line in get_puzzle_input(22, False):
    command, cuboid = line.split()
    coordinates = cuboid.split(",")
    ranges = []
    for coordinate in coordinates:
        r = [int(point) for point in coordinate[2:].split("..")]
        r[1] += 1
        ranges.append(r)
    commands.append([command, ranges])

ranges = []

def clamp(number, minimum, maximum):
    return max(minimum, min(number, maximum))

def clamp_range(slave, master):
    (xmin1, xmax1), (ymin1, ymax1), (zmin1, zmax1) = slave
    (xmin2, xmax2), (ymin2, ymax2), (zmin2, zmax2) = master
    xmin1 = clamp(xmin1, xmin2, xmax2)
    xmax1 = clamp(xmax1, xmin2, xmax2)
    ymin1 = clamp(ymin1, ymin2, ymax2)
    ymax1 = clamp(ymax1, ymin2, ymax2)
    zmin1 = clamp(zmin1, zmin2, zmax2)
    zmax1 = clamp(zmax1, zmin2, zmax2)
    return (xmin1, xmax1), (ymin1, ymax1), (zmin1, zmax1)

def get_area(r):
    return abs((r[0][1] - r[0][0]) * (r[1][1] - r[1][0]) * (r[2][1] - r[2][0]))

# In order to add a range, check for overlaps, delete any overlaps (union) and then simply add the range to the ranges array
def delete(r):
    new_ranges = []
    for r2 in ranges:
        (xmin2, xmax2), (ymin2, ymax2), (zmin2, zmax2) = r2 
        (xmin, xmax), (ymin, ymax), (zmin, zmax) = clamp_range(r, r2)
        top = [(xmin2, xmax2), (ymin2, ymax2), (zmax, zmax2)]
        bottom = [(xmin2, xmax2), (ymin2, ymax2), (zmin2, zmin)]
        left = [(xmin2, xmin), (ymin2, ymax2), (zmin, zmax)]
        right = [(xmax, xmax2), (ymin2, ymax2), (zmin, zmax)]
        front = [(xmin, xmax), (ymin2, ymin), (zmin, zmax)]
        back = [(xmin, xmax), (ymax, ymax2), (zmin, zmax)]
        parts = (top, bottom, left, right, front, back)
        new_ranges += parts if sum(get_area(part) for part in parts) != get_area(r2) else [r2]
    return [ r for r in new_ranges if get_area(r) != 0 ]

def calculate_area():
    area = 0
    for (lx, hx), (ly, hy), (lz, hz) in ranges:
        area += abs((hx - lx) * (hy - ly) * (hz - lz))
    return area

for command in commands:
    ranges = delete(command[1])
    if command[0] == "on":
        ranges.append(command[1])

print(calculate_area())
