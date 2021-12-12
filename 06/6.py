#!/usr/bin/python
fishes = [int(age) for age in next(open("input6")).split(",")]
numbers_of_fish_per_age = [ 0 for i in range(9)]

for fish in fishes:
    numbers_of_fish_per_age[fish] += 1

for i in range(256):
    new_numbers_of_fish_per_age = [ 0 for i in range(9) ]

    for i in range(1, 9):
        if numbers_of_fish_per_age[i] != 0:
            new_numbers_of_fish_per_age[i-1] = numbers_of_fish_per_age[i]
            numbers_of_fish_per_age[i] = 0

    new_numbers_of_fish_per_age[8] = numbers_of_fish_per_age[0]
    new_numbers_of_fish_per_age[6] = numbers_of_fish_per_age[0]
    numbers_of_fish_per_age = new_numbers_of_fish_per_age
    
print("We finish with %d fish" % sum(numbers_of_fish_per_age))
