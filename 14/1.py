from starter import get_puzzle_input
import pdb

lines = get_puzzle_input(14, False)

template, rules = lines[0], [rule.strip().split(' -> ') for rule in lines[2:]]
novo_rules = { rule : result for rule, result in rules }

index = 0
old = [ char for char in template ]
output = []

for i in range(41):
    for j in range(len(old) - 1):
        output.append(old[j])
        output.append(novo_rules[old[j] + old[j+1]])
    output.append(old[-1])
    old = output
    output = []

frequencies = { result : 0 for rule, result in rules }
for value in old:
    frequencies[value] += 1

maximum = max(frequencies, key=frequencies.get)
minimum = min(frequencies, key=frequencies.get)

print(frequencies[maximum] - frequencies[minimum])
