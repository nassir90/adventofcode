from starter import get_puzzle_input
import copy
import math
from itertools import tee
import pdb

def to_array(string, index):
    array = [69, 69]
    index += 1 # discard [
    for i in range(2):
        if string[index] == '[': 
            index, array[i] = to_array(string, index)
        else:
            current_char = string [ index ]
            number_string = ''
            while current_char.isnumeric() or current_char == '-':
                number_string += current_char
                index += 1
                current_char = string[index]
            array[i] = int(number_string)
        index += 1 - i # Discard , if this is the first element
    index += 1 # discard ]
    return index, array

lines = [ to_array(line, 0)[1] for line in get_puzzle_input(18, False) ]
balls, initial_pair = to_array(get_puzzle_input(18, False)[0], 0)

def reduce(cow):
    initial_pair = cow.copy()
    old_pair = []
    
    while old_pair != initial_pair:
        index_stack = [0]
        pair_stack = [ initial_pair ]
        old_pair = copy.deepcopy(initial_pair)

        while len(index_stack) != 0:
            i = index_stack[-1]
            if i <= 1:
                pair = pair_stack[-1]
                if isinstance(pair[i], list):
                    if len(index_stack) == 4:
                        to_explode = index_stack[-1]

                        for towards in 0, 1:
                            psc = pair_stack.copy()
                            xsc = index_stack.copy()
                            change = 1 if towards == 1 else -1
                            while xsc and xsc[-1] == towards:
                                psc.pop()
                                xsc.pop()
                            if xsc:
                                xsc[-1] = towards
                            while xsc:
                                if xsc[-1] == 0 or xsc[-1] == 1:
                                    if isinstance(psc[-1][xsc[-1]], int):
                                        psc[-1][xsc[-1]] += pair[to_explode][towards]
                                        break
                                    else:
                                        psc.append(psc[-1][xsc[-1]])
                                        xsc.append(1 - towards)
                                else:
                                    xsc.pop()
                                    psc.pop()
                                    if xsc:
                                        xsc[-1] += change
                        pair[to_explode] = 0
                        index_stack = [0]
                        pair_stack = [initial_pair]
                    else:
                        index_stack.append(0)
                        pair_stack.append(pair[i])
                else:
                    index_stack[-1] += 1
            else:
                index_stack.pop()
                pair_stack.pop()
                if index_stack:
                    index_stack[-1] += 1

        index_stack = [0]
        pair_stack = [ initial_pair ]

        while len(index_stack) != 0:
            i = index_stack[-1]
            if i <= 1:
                pair = pair_stack[-1]
                if isinstance(pair[i], list):
                    index_stack.append(0)
                    pair_stack.append(pair[i])
                elif pair[i] >= 10:
                    pair[i] = [ math.floor(pair[i] / 2), math.ceil(pair[i] / 2) ]
                    index_stack = [0]
                    pair_stack = [initial_pair]
                    break
                else:
                    index_stack[-1] += 1
            else:
                index_stack.pop()
                pair_stack.pop()
                if index_stack:
                    index_stack[-1] += 1
    return initial_pair

def find_magnitude(pair):
    magnitude = 0
    if isinstance(pair[0], int):
        magnitude += 3 * pair[0]
    else:
        magnitude += 3 * find_magnitude(pair[0])
    if isinstance(pair[1], int):
        magnitude += 2 * pair[1]
    else:
        magnitude += 2 * find_magnitude(pair[1])
    return magnitude

result = lines[0]
for imaginary_number in lines[1:]:
    result = reduce([result, imaginary_number])
print(find_magnitude(result))
