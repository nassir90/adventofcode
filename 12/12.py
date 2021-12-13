from starter import get_puzzle_input

lines = get_puzzle_input(12)

nodes = {}

for line in lines:
    line = line.strip()
    left, right = line.split("-")
    if not nodes.get(left):
        nodes[left] = [right] if right != 'start' and left != 'end' else []
    elif right not in nodes[left] and not (left == 'end' or right == 'start'):
        nodes[left].append(right)
    if not nodes.get(right):
        nodes[right] = [left] if left != 'start' and right != 'end' else []
    elif left not in nodes[right] and not (right == 'end' or left == 'start'):
        nodes[right].append(left)

def recursive_get_paths(start, small_cave_stats):
    path_tail = {}
    for destination in nodes[start]:
        if all(character.isupper() for character in destination) or destination == 'end':
            path_tail[destination] = recursive_get_paths(destination, small_cave_stats)
        elif small_cave_stats[destination] == 0 or max(small_cave_stats.values()) != 2:
            r = small_cave_stats.copy()
            r[destination] += 1
            path_tail[destination] = recursive_get_paths(destination, r)
    return path_tail

paths = { 'start' : {} }

for head in nodes['start']:
    small_cave_stats = { node : 0 if node != head else 1 for node in nodes }
    paths['start'][head] = recursive_get_paths(head, small_cave_stats )

def recursive_format(remainder):
    tails = []
    for child in remainder:
        tails += [child] + [child + "," + tail for tail in recursive_format(remainder[child])]
    return tails

tails = recursive_format(paths)

numero = 0

for head in nodes['start']:
    print("%s > %d" % (head, len([tail for tail in recursive_format(paths['start'][head]) if tail[-3:] == 'end'])))
#        lolz = -2
#        for component in tail.split(","):
#            if all(c.islower() for c in component):
#                lolz += 1
#        if lolz <= 1:
#            numero += 1
