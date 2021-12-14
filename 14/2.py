from starter import get_puzzle_input
import pdb

lines = get_puzzle_input(14, False)

template, rules = lines[0], [rule.strip().split(' -> ') for rule in lines[2:]]
novo_rules = { rule : result for rule, result in rules }

index = 0
printing = False
default_frequencies = {result : 0 for rule, result in rules}
frequency_lists = { i : {} for i in range(100)}

def recursive_find_values(section, remainder=39):
    if section in frequency_lists[remainder]:
        return frequency_lists[remainder][section]

    frequencies = default_frequencies.copy()
    if len(section) == 2:
        new = novo_rules[section]
        left = section[0] + new
        right = new + section[1]
        left_result = novo_rules[left]
        right_result = novo_rules[right]
        if remainder != 0:
            # If the right hand output of this unit is equal to the right hand of the unit,\
            # This is a dead right branch. The contribution of dead branches to the total frequency
            # Array is remainder of it's output
            # Edit: LMAO this did nothing to reduce algorithmic complexity
            # The only thing that helped was remembering the frequencies of previously processed monomer groupings
            if left_result == left[1]:
                new_frequencies_left = default_frequencies.copy()
                if printing: print(left[0], end="")
                frequencies[left[0]] += 1
                for i in range(remainder - 1):
                    new_frequencies = recursive_find_values(left[1] + left[1], i)
                    for key in new_frequencies:
                        new_frequencies_left[key] += new_frequencies[key]
            else:
                new_frequencies_left = recursive_find_values(left, remainder - 1) 

            if right_result == right[0]:
                new_frequencies_right = default_frequencies.copy()
                if printing: print(right[0], end="")
                frequencies[right[0]] += 1
                for i in range(remainder - 1):
                    new_frequencies = recursive_find_values(right[0] + right[0], i)
                    for key in new_frequencies:
                        new_frequencies_right[key] += new_frequencies[key]
            else:
                new_frequencies_right = recursive_find_values(right, remainder - 1) 

            for new_frequencies in new_frequencies_left, new_frequencies_right:
                for key in new_frequencies:
                    frequencies[key] += new_frequencies[key]
        else:
            if printing: print(section[0], end="")
            frequencies[section[0]] += 1
        frequency_lists[remainder][section] = frequencies
    else:
        for i in range(len(section) - 1):
            new_frequencies = recursive_find_values(section[i] + section[i+1], remainder - 1)
            for key in new_frequencies:
                frequencies[key] += new_frequencies[key]
        frequencies[section[-1]] += 1
        frequency_lists[remainder][section] = frequencies
        print(section[-1])
    return frequencies

lols = recursive_find_values(template, 41)
print("3 > " + str(lols))

maximum = next(iter(lols))
minimum = next(iter(lols))

for char in lols:
    if lols[maximum] < lols[char]:
        maximum = char
    if lols[minimum] > lols[char]:
        minimum = char

print(maximum, minimum)

print(lols[maximum] - lols[minimum])
