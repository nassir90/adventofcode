from starter import get_puzzle_input
import copy
import pdb

steps = 50
PADDING = 150

lines = get_puzzle_input(20, False)
encrypt = lines[0]
data = lines[2:]
length_x, length_y = len(data[0]), len(data)

print(length_x, length_y)

blank = [ [ '.' for x in range(2*PADDING+length_x) ] for y in range(2*PADDING+length_y) ]
output = copy.deepcopy(blank)

for y, row in enumerate(data):
    for x, value in enumerate(row):
        output[y+PADDING][x+PADDING] = value

def to_decimal(bits):
    number = 0
    significance = 0
    for bit in reversed(bits):
        number += bit << significance
        significance += 1
    return number

for step in range(steps):
    new_output = copy.deepcopy(blank)
    for y in range(1, len(output) - 1):
        for x in range(1, len(output[0]) - 1):
            bits = output[y-1][x-1:x+2] + output[y][x-1:x+2] + output[y+1][x-1:x+2]
            index = to_decimal([0 if bit == '.' else 1 for bit in bits])
            new_output[y][x] = encrypt[index]
    output = new_output

sum_ = 0

PUDDING=PADDING-PADDING//2

output = [ row[PUDDING:-PUDDING] for row in output[PUDDING:-PUDDING] ]

for row in output:
    print("".join(row))
    for value in row:
        if value == '#':
            sum_ += 1

print("\n%d" % sum_)
