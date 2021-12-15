from starter import get_puzzle_input
import pdb

plot = [ [ int(char) for char in line ] for line in get_puzzle_input(15, False) ]

starting_cost = sum(plot[0]) + sum(line[-1] for line in plot) - plot[0][-1]

print(starting_cost)

# I should remember paths

minimum_cost = starting_cost

def get_neighbors(y, x):
    neighbors = []
    if y != 0:
        neighbors.append((y - 1, x))
    if x != len(plot[0]) - 1:
        neighbors.append((y, x + 1))
    if y != len(plot) - 1:
        neighbors.append((y + 1, x))
    if x != 0:
        neighbors.append((y,x-1))
    return neighbors

def recursive_update_risks(y, x, visited, current_distance, current_distances):
    need_to_check = [(y,x)]
    checked = []
    while len(need_to_check) != 0:
        ones_to_check_next = []
        for y, x in need_to_check:
            if current_distances[y][x] > starting_cost:
                return
            potential_distance = plot[y][x] + current_distances[y][x] 
            for ny, nx in get_neighbors(y,x):
                if (ny,nx) not in checked and (ny,nx) in visited and current_distances[y][x] < current_distances[ny][nx]:
                    current_distances[ny][nx] = potential_distance
                    ones_to_check_next.append((ny,nx))
            checked.append((ny,nx))
        need_to_check = ones_to_check_next

print(plot)

def find_shortest():
    visited = {(0,0)}
    current_distances = [ [ float("Infinity") for x in row ] for row in plot]
    current_distances[0][0] = 0
    plot[0][0] = 0
    just_visited = { (0,0) }
    while len(visited) != len(plot) * len(plot[0]):
        n = []
        for point in just_visited:
            y, x = point
            neighbors = get_neighbors(y, x)
            potential_risk = current_distances[y][x] + plot[y][x]
            for neighbor in get_neighbors(y, x):
                if neighbor not in visited:
                    if potential_risk < current_distances[neighbor[0]][neighbor[1]]:
                        current_distances[neighbor[0]][neighbor[1]] = potential_risk
            for neighbor in get_neighbors(y, x):
                if neighbor in visited:
                    if potential_risk < current_distances[neighbor[0]][neighbor[1]]:
                        current_distances[neighbor[0]][neighbor[1]] = potential_risk
                        recursive_update_risks(y, x, visited, potential_risk, current_distances)
            n += neighbors
        just_visited = { dog for dog in n }
        visited = visited.union(just_visited)
    print(current_distances[-1][-1])

find_shortest()
