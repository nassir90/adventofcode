import copy
import pdb
from starter import get_puzzle_input

OVERLAP_NEEDED = 3

relative_beacon_positions = [[]]
for line in get_puzzle_input(19, False):
    line = line.strip()
    if line:
        relative_beacon_positions[-1].append([int(direction) for direction in line.split(',')])
    else:
        relative_beacon_positions.append([])
print(len(relative_beacon_positions))

relative_beacon_positions = [ [  [0,2,0], [4,1,0], [3,3,0] ], [ [-1,-1,0], [-5,0,0], [-2,1,0] ] ]

adjacent_scanners = []
beacons = 0

def get_z_preserving_rotations(beacon):
    return [[beacon[0], beacon[1], beacon[2]], \
           [beacon[1], -beacon[0], beacon[2]], \
           [-beacon[1], beacon[0], beacon[2]], \
           [-beacon[0], -beacon[1], beacon[2]]]

def get_rotations(beacon):
    #rotations = [[] for i in range(len(beacons))]
    #for index, beacon in enumerate(beacons):
    rotations = []
    rotations += get_z_preserving_rotations([beacon[0], beacon[1], beacon[2]])
    rotations += get_z_preserving_rotations([beacon[2], beacon[1], -beacon[0]])
    rotations += get_z_preserving_rotations([-beacon[2], beacon[1], beacon[0]])
    rotations += get_z_preserving_rotations([-beacon[0], beacon[1], -beacon[2]])
    rotations += get_z_preserving_rotations([beacon[0], beacon[2], -beacon[1]])
    rotations += get_z_preserving_rotations([beacon[0], -beacon[2], beacon[1]])
    return rotations

for phase in range(len(relative_beacon_positions) - 1):
    standard = relative_beacon_positions[phase]
    pre_standard_objectification = standard[-1].copy()
    for beacon_index, beacon in enumerate(standard):
        standard_origin = beacon[0], beacon[1], beacon[2]
        # Objecivisation of scanner with beacon as 0, 0
        for beacon in standard:
            beacon[0] -= standard_origin[0]
            beacon[1] -= standard_origin[1]
            beacon[2] -= standard_origin[2]
        adjacent = False
        for index, comparand in enumerate(relative_beacon_positions[phase+1:]):
            pre_comparand_objectification = copy.deepcopy(comparand)
            for i in range(len(comparand)):
                comparand[i] = get_rotations(comparand[i])
            for rotation in range(24):
                for comparand_index, comparand_beacon in enumerate(comparand):
                    comparand_origin = comparand_beacon[rotation].copy()

                    # Objectification 
                    for beacon_rotations in comparand:
                        beacon_rotations[rotation][0] -= comparand_origin[0]
                        beacon_rotations[rotation][1] -= comparand_origin[1]
                        beacon_rotations[rotation][2] -= comparand_origin[2]

                    print()
                    common = 0
                    for comparand_beacon in comparand: # Comparand is a scanner
                        for standard_beacon in standard:
                            if comparand_beacon[rotation] == standard_beacon:
                                common += 1
                                #print(common, [comparand[0][rotation], comparand[1][rotation], comparand[2][rotation]], standard)
                                print(standard_beacon)

                    if common >= OVERLAP_NEEDED:
                        adjacent = True
                        adjacent_scanners.append([phase, index + phase + 1, beacon_index, comparand_index, rotation])
                        break
            for i in range(len(comparand)):
                comparand[i] = comparand[i][0]
            pre_comparand_objectification = pre_comparand_objectification[comparand.index([0,0,0])]
            for beacon in comparand:
                beacon[0] += pre_comparand_objectification[0]
                beacon[1] += pre_comparand_objectification[1]
                beacon[2] += pre_comparand_objectification[2]
        if adjacent:
            break
    # Restoration of standard scanner
    for beacon in standard:
        beacon[0] += pre_standard_objectification[0]
        beacon[1] += pre_standard_objectification[1]
        beacon[2] += pre_standard_objectification[2]

print(adjacent_scanners)
