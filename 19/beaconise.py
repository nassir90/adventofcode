import json
import pdb
import datetime
from starter import get_puzzle_input
from rotations import get_rotations
import copy

OVERLAP_NEEDED = 12

scanners = [[]]
for line in get_puzzle_input(19, False):
    line = line.strip()
    if line:
        scanners[-1].append([int(direction) for direction in line.split(',')])
    else:
        scanners.append([])

if len(scanners) > 20:
    a, ad = json.load(open("./19-04.aad"))
else:
    a, ad = json.load(open("./04-04.aad"))

def fill(start, aligned):
    for i, c in enumerate(a):
        if c[0] == start and not aligned[c[1]]:
            aligned[c[1]] = True
            fill(c[1], aligned)
        elif c[1] == start and aligned[c[1]] and not aligned[c[0]]:
            # Swap scanner IDs
            temp = c[1]
            c[1] = c[0]
            c[0] = temp
            # Swap LC indices
            temp = ad[i][1][1]
            ad[i][1][1] = ad[i][1][0]
            temp = ad[i][1][0] = temp
            aligned[c[1]] = True
            fill(c[1], aligned)

aligned = [True] + [False for i in range(len(scanners) - 1)]

fill(0, aligned)
print(a)
print(ad)
print(all(aligned), aligned)

def beaconise(index, position, rotation_stack, positioned):
    for i, link in enumerate(a):
        if link[0] != index or link[1] in positioned:
            continue
        oriented_beacons[link[1]] = copy.deepcopy(scanners[link[1]])
        new_rotation_stack = rotation_stack + [ad[i][0]]
        for rotation in reversed(new_rotation_stack):
            for j in range(len(oriented_beacons[1])):
                oriented_beacons[link[1]][j] = get_rotations(oriented_beacons[link[1]][j])[rotation]
        positioned_beacons[link[1]] = copy.deepcopy(oriented_beacons[link[1]])

        source_index = ad[i][1][0]
        destination_index = ad[i][1][1]
        
        source_position = oriented_beacons[index][source_index]
        destination_position = oriented_beacons[link[1]][destination_index]

        p = [
            position[0] + source_position[0] - destination_position[0],
            position[1] + source_position[1] - destination_position[1],
            position[2] + source_position[2] - destination_position[2]
        ]

        for beacon in positioned_beacons[link[1]]:
            beacon[0] += p[0]
            beacon[1] += p[1]
            beacon[2] += p[2]
        positioned.append(link[1])

        print(index, position, link[1], p)
        
        beaconise(link[1], p, new_rotation_stack, positioned)

positioned_beacons =[[] for i in range(len(scanners))] 
oriented_beacons = [[] for i in range(len(scanners))]

oriented_beacons[0] = scanners[0]
positioned_beacons[0] = scanners[0]

beaconise(0, [0,0,0], [], [0])

for positioned_scanner in positioned_beacons:
    for beacon in positioned_scanner:
        print(beacon)
