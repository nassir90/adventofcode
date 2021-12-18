from starter import get_puzzle_input
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

balls, initial_pair = to_array(get_puzzle_input(18, False)[0], 0)

index_stack = [0]
pair_stack = [ initial_pair ]

while len(index_stack) != 0:
    i = index_stack[-1]
    if i <= 1:
        pair = pair_stack[-1]
        print(pair[i])
        if isinstance(pair[i], int):
            if pair[i] >= 10:
                pair[i] = [ math.floor(pair[i] / 2), math.ceil(pair[i] / 2) ]
                index_stack = [0]
                pair_stack = [initial_pair]
            index_stack[-1] += 1
        else:
            to_explode = index_stack[-1]
            if isinstance(pair[to_explode], list):
                print("here brah " + str(pair))
                if len(index_stack) == 4:
                    change = 1 if to_explode == 0 else -1
                    for to_add_to in 0, 1:
                        ps_clone = pair_stack.copy()
                        is_clone = index_stack.copy()
                        if to_explode == to_add_to:
                            while is_clone and is_clone[-1] == to_add_to:
                                is_clone.pop()
                                ps_clone.pop()
                        if is_clone:
                            is_clone[-1] = to_add_to
                        while is_clone:
                            if is_clone[-1] < 0 or is_clone[-1] < 2:
                                pdb.set_trace()
                                if isinstance(ps_clone[-1][is_clone[-1]], int):
                                    ps_clone[-1][is_clone[-1]] += pair[to_explode][to_add_to]
                                    break
                                else:
                                    ps_clone.append(ps_clone[-1][is_clone[-1]])
                                    is_clone.append( to_add_to)
                                    is_clone[-2] += change
                            else:
                                while len(is_clone) != 0 and is_clone[-1] != to_add_to:
                                    is_clone.pop()
                                    ps_clone.pop()
                    pair[to_explode] = 0
                    index_stack = [0]
                    pair_stack = [initial_pair]
                else:
                    index_stack[-1] += 1
                    index_stack.append(0)
                    pair_stack.append(pair[i])
    else:
        index_stack.pop()
        pair_stack.pop()
        if index_stack:
            index_stack[-1] += 1

print(initial_pair)
