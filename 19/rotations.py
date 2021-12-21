def get_z_preserving_rotations(b):
    return [[b[0], b[1], b[2]], \
           [b[1], -b[0], b[2]], \
           [-b[1], b[0], b[2]], \
           [-b[0], -b[1], b[2]]]

def get_rotations(b):
    rotations = []
    rotations += get_z_preserving_rotations([b[0], b[1], b[2]])
    rotations += get_z_preserving_rotations([b[2], b[1], -b[0]])
    rotations += get_z_preserving_rotations([-b[2], b[1], b[0]])
    rotations += get_z_preserving_rotations([-b[0], b[1], -b[2]])
    rotations += get_z_preserving_rotations([b[0], b[2], -b[1]])
    rotations += get_z_preserving_rotations([b[0], -b[2], b[1]])
    return rotations
