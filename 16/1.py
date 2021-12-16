from starter import get_puzzle_input
import pdb

def decimal(array):
    significance = 1
    number = 0
    for digit in reversed(array):
        number += significance * digit
        significance *= 2
    return number

binary = {
    "0":[0,0,0,0],
    "1":[0,0,0,1],
    "2":[0,0,1,0],
    "3":[0,0,1,1],
    "4":[0,1,0,0],
    "5":[0,1,0,1],
    "6":[0,1,1,0],
    "7":[0,1,1,1],
    "8":[1,0,0,0],
    "9":[1,0,0,1],
    "A":[1,0,1,0],
    "B":[1,0,1,1],
    "C":[1,1,0,0],
    "D":[1,1,0,1],
    "E":[1,1,1,0],
    "F":[1,1,1,1]
}
code = [ number for piece in get_puzzle_input(16, False)[0] for number in binary[piece]]

digits = iter(code)
packet_length_stack = [[1,1,0]] #length_type, length, bits_read, values, type_of_packet
versions = []

while len(packet_length_stack) != 0:
    length_type, length, bits_read = packet_length_stack[-1]
    if length_type == 1 and length > 0 or length_type == 0 and bits_read < length:
        if length_type == 1:
            packet_length_stack[-1][1] -= 1
        version = [ next(digits), next(digits), next(digits) ]
        versions.append(decimal(version))
        type_of_this_packet = decimal([ next(digits), next(digits), next(digits) ])
        packet_length_stack[-1][2] += 6
        if type_of_this_packet == 4:
            literal = []
            while next(digits) == 1:
                literal += [ next(digits), next(digits), next(digits), next(digits) ]
            literal += [ next(digits), next(digits), next(digits), next(digits) ]
            packet_length_stack[-1][2] += len(literal) + len(literal) // 4
        else:
            this_length_type = next(digits)
            bits_to_read = 15 if this_length_type == 0 else 11
            packet_length_stack[-1][2] += 1 + bits_to_read
            packet_length_stack.append( \
                    [this_length_type, \
                    decimal([next(digits) for i in range(bits_to_read)]), \
                    0 ])
    else:
        packet_length_stack.pop()

        if len(packet_length_stack) != 0:
            packet_length_stack[-1][2] += bits_read
print(sum(versions))
