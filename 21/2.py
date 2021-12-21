from starter import get_puzzle_input
import pdb

lolz = [(1, (7, 4), (0, 0))]
results = {i:0 for i in range(21)}

def get_multiplicity(roll):
    return [1, 3, 6, 7, 6, 3, 1][roll-3]

def advance_position(position, amount):
    return ( position + amount ) % 10

w1 = 0
w2 = 0

while lolz:
    new_lolz = []
    for m, (p1, p2), (s1, s2) in lolz:
        for roll in range(3,10):
            new_m1 = m * get_multiplicity(roll)
            new_p1 = advance_position(p1, roll)
            new_s1 = s1 + new_p1 + 1
            if new_s1 >= 21:
                w1 += new_m1
            else:
                for r2 in range(3, 10):
                    new_m2 = new_m1 * get_multiplicity(r2)
                    new_p2 = advance_position(p2, r2)
                    new_s2 = s2 + new_p2 + 1
                    if new_s2 >= 21:
                        w2 += new_m2
                    else:
                        new_lolz.append((new_m2, (new_p1, new_p2), (new_s1, new_s2)))
    lolz = new_lolz

print(w1, w2)
