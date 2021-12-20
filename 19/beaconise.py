import json
import datetime
from starter import get_puzzle_input
import copy

OVERLAP_NEEDED = 12

scanners = [[]]
for line in get_puzzle_input(19, False):
    line = line.strip()
    if line:
        scanners[-1].append([int(direction) for direction in line.split(',')])
    else:
        scanners.append([])

original_scanners = copy.deepcopy(scanners)

if len(scanners) > 20:
    a, ad = json.load(open("./19-04.aad"))
else:
    a, ad = json.load(open("./04-04.aad"))

def derotate(beacon, rotation):
    non_z_prev = rotation // 4
    z_prev = rotation % 4
    
    beacon = [
        [beacon[0], beacon[1], beacon[2]],
        [-beacon[2], beacon[1], beacon[0]],
        [beacon[2], beacon[1], -beacon[0]],
        [-beacon[0], beacon[1], -beacon[2]],
        [beacon[0], -beacon[2], beacon[1]],
        [beacon[0], beacon[2], -beacon[1]]
    ][non_z_prev]
    
    beacon = [
        [beacon[0], beacon[1], beacon[2]],
        [-beacon[1], beacon[0], beacon[2]],
        [beacon[1], -beacon[0], beacon[2]],
        [-beacon[0], -beacon[1], beacon[2]]
    ][z_prev]

    return beacon

def get_z_preserving_rotations(b):
    return [[b[0], b[1], b[2]], \
           [b[1], -b[0], b[2]], \
           [-b[1], b[0], b[2]], \
           [-b[0], -b[1], b[2]]]

def get_rotations(b):
    #rotations = [[] for i in range(len(bs))]
    #for index, b in enumerate(bs):
    rotations = []
    rotations += get_z_preserving_rotations([b[0], b[1], b[2]])
    rotations += get_z_preserving_rotations([b[2], b[1], -b[0]])
    rotations += get_z_preserving_rotations([-b[2], b[1], b[0]])
    rotations += get_z_preserving_rotations([-b[0], b[1], -b[2]])
    rotations += get_z_preserving_rotations([b[0], b[2], -b[1]])
    rotations += get_z_preserving_rotations([b[0], -b[2], b[1]])
    return rotations


def compute_rotation(s1i, s2i):
    rot = None
    s1 = scanners[s1i]
    o1 = copy.deepcopy(s1)
    for b1 in s1:
        h1 = b1.copy()
        for b in s1:
            b[0] -= h1[0]
            b[1] -= h1[1]
            b[2] -= h1[2]
        adjacent = False
        s2 = scanners[s2i]
        for i in range(len(s2)):
            s2[i] = get_rotations(s2[i])
        for r in range(24):
            o2 = [ b[r] for b in copy.deepcopy(s2) ]
            for b2i, b2 in enumerate(s2):
                h2 = b2[r].copy()
                for b in s2:
                    b[r][0] -= h2[0]
                    b[r][1] -= h2[1]
                    b[r][2] -= h2[2]
                c = 0
                impossible = False
                for b1i, b1 in enumerate(s1):
                    for bi, b in enumerate(s2):
                        if (len(s1) - b1i) * (len(s2) - bi) < OVERLAP_NEEDED - c:
                            impossible = True
                            break
                        if b[r] == b1:
                            c += 1
                    if impossible:
                        break
                if c >= OVERLAP_NEEDED:
                    rot = r
            n2 = [ b[r] for b in s2 ]
            r2 = o2[n2.index([0,0,0])]
            for b in n2:
                b[0] += r2[0]
                b[1] += r2[1]
                b[2] += r2[2]
            if adjacent:
                break
        for i in range(len(s2)):
            s2[i] = s2[i][0]
    restore1 = o1[s1.index([0,0,0])]
    for b in s1:
        b[0] += restore1[0]
        b[1] += restore1[1]
        b[2] += restore1[2]
    return rot

def fill(start, aligned):
    for i, c in enumerate(a):
        if c[0] == start and not aligned[c[1]]:
            aligned[c[1]] = True
            fill(c[1], aligned)
        elif c[1] == start and not aligned[c[0]]:
            temp = c[1]
            c[1] = c[0]
            c[0] = temp
            temp = ad[i][1][1]
            ad[i][1][1] = ad[i][1][0]
            temp = ad[i][1][0] = temp
            aligned[c[1]] = True
            fill(c[1], aligned)

aligned = [True] + [False for i in range(len(scanners) - 1) ]

fill(0, aligned)
print(a,ad)
print(all(aligned), aligned)

def beaconise(index, position, rotation_stack, beaconised):
    for i, cousins in enumerate(a):
        if cousins[0] != index or cousins[1] in beaconised:
            continue
        beaconised.append(cousins[1])
        correctly_oriented_beacons[cousins[1]] = copy.deepcopy(original_scanners[cousins[1]])
        new_rotation_stack = rotation_stack + [ad[i][0]]
        for rotation in reversed(new_rotation_stack):
            for j in range(len(correctly_oriented_beacons[cousins[1]])):
                correctly_oriented_beacons[cousins[1]][j] = get_rotations(correctly_oriented_beacons[cousins[1]][j])[rotation]
        correct_beacons[cousins[1]] = copy.deepcopy(correctly_oriented_beacons[cousins[1]])

        source_index = ad[i][1][0]
        destination_index = ad[i][1][1]
        
        source_position = correctly_oriented_beacons[index][source_index]
        destination_position = correctly_oriented_beacons[cousins[1]][destination_index]

        p = [
            position[0] + source_position[0] - destination_position[0],
            position[1] + source_position[1] - destination_position[1],
            position[2] + source_position[2] - destination_position[2]
        ]

        print(cousins[0], position, cousins[1], p)

        for beacon in correct_beacons[cousins[1]]:
            beacon[0] += p[0]
            beacon[1] += p[1]
            beacon[2] += p[2]
        
        beaconise(cousins[1], p, new_rotation_stack, beaconised)


correct_beacons =[[] for i in range(len(scanners))] 
correctly_oriented_beacons = [[] for i in range(len(scanners))]

correctly_oriented_beacons[0] = original_scanners[0]
correct_beacons[0] = original_scanners[0]

beaconise(0, [0,0,0], [], [0])

for correct_scanner in correct_beacons:
    for beacon in correct_scanner:
        print(beacon)
