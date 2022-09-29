import rotations

# Takes two detected beacon 3D arrays If the arrays can be rectified,
# this array returns the positions of the points in the rectifend
# relative to those in the rectaum. If the arrays cannot be rectified,
# this function returns none

scanner_positions = []

def rectify(rectifend, rectaum):
    map_list = list(rectifend)
    map_clone = [list(point) for point in map_list]
    for i, map_anchor in enumerate(map_clone):
        map_anchor_clone = map_anchor.copy()
        for point in map_clone:
            point[0] -= map_anchor_clone[0]
            point[1] -= map_anchor_clone[1]
            point[2] -= map_anchor_clone[2]
        for center_of_rotation in rectaum:
            center_of_rotation_clone = center_of_rotation.copy()
            for point in rectaum:
                point[0] -= center_of_rotation_clone[0]
                point[1] -= center_of_rotation_clone[1]
                point[2] -= center_of_rotation_clone[2]
            assert tuple(center_of_rotation) == tuple(map_anchor) == (0,0,0)
            rectified, r = rotation_where_overlap_occurs(map_clone, rectaum)
            if rectified:
                beacons = [(point[0]+map_list[i][0],
                            point[1]+map_list[i][1],
                            point[2]+map_list[i][2]) for point in rectified]
                scanner_position = beacons.pop()
                return beacons, scanner_position
    return None, None

# Takes an array of beacons and for each of the 24 relevant rotations,
# runs predicate on it.
def rotation_where_overlap_occurs(rectifend, beacons):
    for i, rotation in enumerate(zip(*tuple(rotations.get_rotations(point) for point in beacons))):
        rectifend_set = set(tuple(tuple(point) for point in rectifend))
        intersection = len(rectifend_set.intersection(rotation[:-1]))
        if intersection >= share_threshold:
            return rotation, i
    return None, None

detected_beacons_per_scanner = []
detected_beacons = []
share_threshold = 12

for line in open("input"):
    beacon_points = line.split(",")
    if len(beacon_points) == 1:
        detected_beacons.append([0,0,0]) # Put the scanner center at the end
        detected_beacons_per_scanner.append(detected_beacons)
        detected_beacons = []
    else:
        detected_beacons.append([int(part) for part in beacon_points])

map = set([tuple(point) for point in detected_beacons_per_scanner.pop(0)[:-1]])

while len(detected_beacons_per_scanner) != 0:
    unrectified_beacon_points = detected_beacons_per_scanner.pop(0)
    beacon_points_in_map, scanner_position = rectify(map, unrectified_beacon_points)
    if beacon_points_in_map:
        scanner_positions.append(scanner_position)
        map = map.union([tuple(point) for point in beacon_points_in_map])
        print(f"Map size is now {len(map)}")
    else:
        print("...")
        detected_beacons_per_scanner.append(unrectified_beacon_points)

# print("\nDONE\n")

# for point in map:
    # print(f"{point[0]}, {point[1]}, {point[2]}")

# print(f"\n{len(map)}")


for point in scanner_positions:
    print(f"{point[0]}, {point[1]}, {point[2]}")
print(len(map))
