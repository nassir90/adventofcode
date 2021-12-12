import pdb

file = open("example3")
lines = [ line.strip() for line in file ]

def find_gamma(lines, ox: bool):
    gamma = [ 0 for i in range(12) ]
    number_of_lines = 0
    for line in lines:
        number_of_lines += 1
        for index, char in enumerate(line.strip()):
            gamma[index] += 1 if char == '1' else 0
    return [ place / number_of_lines > 0.5 or place / number_of_lines == 0.5 and ox for place in gamma ]

def find_epsilon(gamma):
    return [ not place for place in gamma ]

def find_co2_rating(lines, bit: int):
    gamma = find_gamma(lines, True);
    gamma = find_epsilon(gamma);
    
    new_lines = [ line for line in lines if line[bit] == str(int(gamma[bit])) ]

    if len(new_lines) == 1:
        return new_lines[0]
    elif len(new_lines) != 0:
        return find_co2_rating(new_lines, bit + 1)
    else:
        print("Error, reached zero length")

def find_oxygen_scrubber_rating(lines, bit: int):
    gamma = find_gamma(lines, True);
    
    new_lines = [ line for line in lines if line[bit] == str(int(gamma[bit])) ]

    if len(new_lines) == 1:
        return new_lines[0]
    elif len(new_lines) != 0:
        return find_oxygen_scrubber_rating(new_lines, bit + 1)
    else:
        print("Error, reached zero length")

oxygen_scrubber_rating = find_oxygen_scrubber_rating(lines, 0)
co2_rating = find_co2_rating(lines, 0)

print("".join(str(int(x)) for x in oxygen_scrubber_rating))
print("".join(str(int(x)) for x in co2_rating))
