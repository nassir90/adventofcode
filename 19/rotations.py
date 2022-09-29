def get_z_preserving_rotations(b):
    return (b[0], b[1], b[2]), \
           (b[1], -b[0], b[2]), \
           (-b[1], b[0], b[2]), \
           (-b[0], -b[1], b[2])

def get_rotations(b):
    return (*get_z_preserving_rotations([b[0], b[1], b[2]]),
            *get_z_preserving_rotations([b[2], b[1], -b[0]]),
            *get_z_preserving_rotations([-b[2], b[1], b[0]]),
            *get_z_preserving_rotations([-b[0], b[1], -b[2]]),
            *get_z_preserving_rotations([b[0], b[2], -b[1]]),
            *get_z_preserving_rotations([b[0], -b[2], b[1]]))

def visualize_rotations(point):
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('TkAgg')
    points = get_rotations(point)
    xs, ys, zs = list(zip(*points))
    figure, axes = plt.subplots(1, 1, subplot_kw={'projection':'3d'})
    axes.scatter(xs,ys,zs)
    figure.show()
    plt.show()
