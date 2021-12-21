from starter import get_puzzle_input
import pdb

current = -1

def advance_position(position, amount):
    return ( position + amount ) % 10

def deterministic_roll():
    global current
    current = ( current + 1 ) % 100
    return current

p1 = 3
p2 = 7
s1 = 0
s2 = 0
rolls = 0

while True:
    p1 = advance_position(p1, 3 + deterministic_roll() + deterministic_roll() + deterministic_roll())
    s1 += p1 + 1
    rolls += 3
    if s1 >= 1000:
        break
    p2 = advance_position(p2, 3 + deterministic_roll() + deterministic_roll() + deterministic_roll())
    s2 += p2 + 1
    rolls += 3
    if s2 >= 1000:
        break

print(s1,s2,p1,p2,rolls)
print(min(s1,s2)*rolls)
