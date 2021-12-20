from starter import get_puzzle_input
import json
import datetime
import copy
import pdb

debug = True
OVERLAP_NEEDED = 12

scanners = [[]]
for line in get_puzzle_input(19, False):
    line = line.strip()
    if line:
        scanners[-1].append([int(direction) for direction in line.split(',')])
    else:
        scanners.append([])

original_scanners = copy.deepcopy(scanners)

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

a = []
ad = []

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
        if [s1i, s2i] in a:
            continue
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

print(compute_rotation(1,0))

for s1i in range(len(scanners) - 1):
    s1 = scanners[s1i]
    o1 = copy.deepcopy(s1)
    for b1 in s1:
        h1 = b1.copy()
        for b in s1:
            b[0] -= h1[0]
            b[1] -= h1[1]
            b[2] -= h1[2]
        adjacent = False
        for s2i in range(s1i + 1, len(scanners)):
            s2 = scanners[s2i]
            if [s1i, s2i] in a:
                continue
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
                    lc = None
                    impossible = False
                    for b1i, b1 in enumerate(s1):
                        for bi, b in enumerate(s2):
                            if (len(s1) - b1i) * (len(s2) - bi) < OVERLAP_NEEDED - c:
                                impossible = True
                                break
                            if b[r] == b1:
                                c += 1
                                lc = (b1i, bi)
                        if impossible:
                            break
                    if c >= OVERLAP_NEEDED:
                        adjacent = True
                        a.append([s1i, s2i])
                        ad.append([r, lc])
                        if debug: print("Scanner %d and scanner %d are adjacent with rotation %d" % (s1i, s2i, r))
                        break
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

if debug: print(list(zip(a,ad)))

json.dump([a,ad], open(datetime.datetime.now().strftime("%H-%M.aad"), "w"))

def derotate(beacon, rotation):
    non_z_prev = rotation // 4
    z_prev = rotation % 4
    
    beacon = [
        [beacon[0], beacon[1], beacon[2]],
        [-beacon[1], beacon[0], beacon[2]],
        [beacon[1], -beacon[0], beacon[2]],
        [-beacon[0], -beacon[1], beacon[2]]
    ][z_prev]

    
    beacon = [
        [beacon[0], beacon[1], beacon[2]],
        [-beacon[2], beacon[1], beacon[0]],
        [beacon[2], beacon[1], -beacon[0]],
        [-beacon[0], beacon[1], -beacon[2]],
        [beacon[0], -beacon[2], beacon[1]],
        [beacon[0], beacon[2], -beacon[1]]
    ][non_z_prev]

    return beacon

correct_beacons = [[] for i in range(len(scanners))]

def beaconise(index, position, rotation_stack):
    pdb.set_trace()
    beaconised = []
    for i, cousins in enumerate(a):
        if cousins[0] != index:
            continue
        correct_beacons[cousins[1]] = copy.deepcopy(original_scanners[cousins[1]])
        new_rotation_stack = rotation_stack + [ad[i][0]]
        for rotation in new_rotation_stack:
            for j in range(len(correct_beacons[cousins[1]])):
                print()
                print(correct_beacons[cousins[1]][j])
                correct_beacons[cousins[1]][j] = derotate(correct_beacons[cousins[1]][j], rotation)
                print(correct_beacons[cousins[1]][j])

        source_index = ad[i][1][0]
        destination_index = ad[i][1][1]
        
        source_position = correct_beacons[index][source_index]
        destination_position = correct_beacons[cousins[1]][destination_index]
        
        print(source_position, destination_position)

        p = [
            position[0] + source_position[0] - destination_position[0],
            position[1] + source_position[1] - destination_position[1],
            position[2] + source_position[2] - destination_position[2]
        ]

        print(cousins[0], position)

        for beacon in correct_beacons[cousins[1]]:
            beacon[0] += p[0]
            beacon[1] += p[1]
            beacon[2] += p[2]
        
        beaconise(cousins[1], p, new_rotation_stack)
    return correct_beacons

correct_beacons[0] = scanners[0]

beaconise(0, [0,0,0], [])
