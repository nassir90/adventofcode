from starter import get_puzzle_input
import pdb

lines = get_puzzle_input(14, False)

template, rules = lines[0], [rule.strip().split(' -> ') for rule in lines[2:]]
novo_rules = { rule : result for rule, result in rules }
printing = False
default_frequencies = { result : 0 for rule, result in rules }
frequency_lists = { i : {} for i in range(100)}

def recursive_find_values(section, remainder=39):
    if section in frequency_lists[remainder]:
        return frequency_lists[remainder][section]

    frequencies = default_frequencies.copy()

    for index in range (len(section) - 1):
        subsection = section[index] + section[index+1]
        new = novo_rules[subsection]
        left = subsection[0] + new
        right = new + subsection[1]
        if remainder != 0:
            new_frequencies_left = recursive_find_values(left, remainder - 1) 
            new_frequencies_right = recursive_find_values(right, remainder - 1) 
            for new_frequencies in new_frequencies_left, new_frequencies_right:
                for key in new_frequencies:
                    frequencies[key] += new_frequencies[key]
        else:
            if printing: print(subsection[0], end="")
            frequencies[subsection[0]] += 1
    if len(section) != 2: # This is the main function
        frequencies[section[-1]] += 1
        if printing: print(section[-1])
    frequency_lists[remainder][section] = frequencies
    return frequencies

frequencies = recursive_find_values(template, 40)

minimum = min(frequencies, key=frequencies.get)
print(frequencies[maximum] - frequencies[minimum])
