from starter import get_puzzle_input
from rotations import get_rotations
import copy

OVERLAP_NEEDED = 3

scanners = [[]]
for line in get_puzzle_input(19, False):
    line = line.strip()
    if line:
        scanners[-1].append([int(direction) for direction in line.split(',')])
    else:
        scanners.append([])

for scanner in 
