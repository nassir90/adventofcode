from starter import get_puzzle_input
import math

closers = "]>)}"
corrupted_indices = []
puzzle_input = get_puzzle_input(10)
total_score = 0

for index, line in enumerate(puzzle_input):
    expected_closer = []
    errors = ""
    for char in line:
        if char == "<":
            expected_closer.append(">")
        elif char == "(":
            expected_closer.append(")")
        elif char == "[":
            expected_closer.append("]")
        elif char == "{":
            expected_closer.append("}")
        elif char in closers:
            if len(expected_closer) != 0:
                if char != expected_closer.pop():
                    errors += char
            else:
                continue
    score = 0
    for char in errors:
        if char == ")":
            score += 3
        elif char == "]":
            score += 57
        elif char == "}":
            score += 1197
        elif char == ">":
            score += 25137
    if score != 0:
        total_score += score
        corrupted_indices.append(index)

print(total_score)

# part 2 

scores = []
        
for index, line in enumerate(puzzle_input):
    if index in corrupted_indices: # BAD
        continue
    expected_closer = []
    errors = ""
    for char in line:
        if char == "<":
            expected_closer.append(">")
        elif char == "(":
            expected_closer.append(")")
        elif char == "[":
            expected_closer.append("]")
        elif char == "{":
            expected_closer.append("}")
        elif len(expected_closer) != 0 and char in closers:
            expected_closer.pop()
    score = 0
    for char in reversed(expected_closer):
        score *= 5
        if char == ")":
            score += 1
        elif char == "]":
            score += 2
        elif char == "}":
            score += 3
        elif char == ">":
            score += 4
    scores.append(score)

scores.sort()
print(scores[math.floor(len(scores) / 2)])
