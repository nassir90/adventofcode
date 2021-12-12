from starter import get_puzzle_input

data = [ int(position) for position in get_puzzle_input(7)[0].split(",") ]
minimum_position = min(data)
maximum_position = max(data)
minimum_fuel_usage = 99999999999999999

def sum_(n):
    return (n*n + n) / 2

for position in range(minimum_position, maximum_position + 1):
    this_fuel_usage = 0
    for crab in data:
        this_fuel_usage += sum_(abs(crab - position))
    if minimum_fuel_usage > this_fuel_usage:
        minimum_fuel_usage = this_fuel_usage

print(minimum_fuel_usage)
