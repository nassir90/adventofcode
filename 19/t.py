def get_z_preserving_rotations(b):
    return [[b[0], b[1], b[2]], \
           [b[1], -b[0], b[2]], \
           [-b[1], b[0], b[2]], \
           [-b[0], -b[1], b[2]]]

def get_rotations(b):
    #rotations = [[] for i in range(len(bs))]
    #for index, b in enumerate(bs):
    rotations = []
    rotations += get_z_preserving_rotations([b[0], b[1], b[2]])
    rotations += get_z_preserving_rotations([b[2], b[1], -b[0]])
    rotations += get_z_preserving_rotations([-b[2], b[1], b[0]])
    rotations += get_z_preserving_rotations([-b[0], b[1], -b[2]])
    rotations += get_z_preserving_rotations([b[0], b[2], -b[1]])
    rotations += get_z_preserving_rotations([b[0], -b[2], b[1]])
    return rotations

def derotate(beacon, rotation):
    non_z_prev = rotation // 4
    z_prev = rotation % 4
    
    beacon = [
        [beacon[0], beacon[1], beacon[2]],
        [-beacon[1], beacon[0], beacon[2]],
        [beacon[1], -beacon[0], beacon[2]],
        [-beacon[0], -beacon[1], beacon[2]]
    ][z_prev]

    
    beacon = [
        [beacon[0], beacon[1], beacon[2]],
        [-beacon[2], beacon[1], beacon[0]],
        [beacon[2], beacon[1], -beacon[0]],
        [-beacon[0], beacon[1], -beacon[2]],
        [beacon[0], -beacon[2], beacon[1]],
        [beacon[0], beacon[2], -beacon[1]]
    ][non_z_prev]

    return beacon

rot = get_rotations([1,2,3])[12]
rot2 = get_rotations(rot)[5]
print(rot2)
rot3 = derotate(rot2, 5)
print(rot3)
rot4 = derotate(rot3, 12)
print(rot4)
