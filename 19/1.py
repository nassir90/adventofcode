from starter import get_puzzle_input
import json
import datetime
import copy
import pdb
from rotations import get_rotations

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

a = []
ad = []

for s1i in range(len(scanners) - 1):
    s1 = scanners[s1i]
    o1 = copy.deepcopy(s1)
    for b1 in s1:
        # Objectify b
        h1 = b1.copy()
        for b in s1:
            b[0] -= h1[0]
            b[1] -= h1[1]
            b[2] -= h1[2]
        adjacent = False
        for s2i in range(s1i + 1, len(scanners)):
            if [s1i, s2i] in a:
                continue
            s2 = scanners[s2i]
            o2 = copy.deepcopy(s2)
            for i in range(len(s2)):
                s2[i] = get_rotations(s2[i])
            for r in range(24):
                for b2i, b2 in enumerate(s2):
                    # Objectify b2
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
                                lc = [b1i, bi]
                        if impossible:
                            break
                    if c >= OVERLAP_NEEDED:
                        adjacent = True
                        a.append([s1i, s2i])
                        ad.append([r, lc])
                        if debug: print("Scanner %d and scanner %d are adjacent with rotation %d" % (s1i, s2i, r))
                        break
                if adjacent:
                    break
            for i in range(len(s2)):
                s2[i] = s2[i][0]
            for b in s2:
                b[0] += o2[-1][0]
                b[1] += o2[-1][1]
                b[2] += o2[-1][2]
    for b in s1:
        b[0] += o1[-1][0]
        b[1] += o1[-1][1]
        b[2] += o1[-1][2]

if debug: print(list(zip(a,ad)))

json.dump([a,ad], open(datetime.datetime.now().strftime("neo-%H-%M.json"), "w"))
