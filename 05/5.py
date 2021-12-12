import pdb

lines = []

for line in open("input"):
    pair = [ coordinate.split(',') for coordinate in line.split(' -> ') ]
    lines.append(pair[0] + pair[1])

maximum_x = 0
maximum_y = 0
horizontal_lines = []
vertical_lines = []
diagonal_lines = []

for points in lines:
    x1 = int(points[0])
    y1 = int(points[1])
    x2 = int(points[2])
    y2 = int(points[3])

    if y1 == y2:
        horizontal_lines.append([x1,y1,x2,y2])
    elif x1 == x2:
        vertical_lines.append([x1,y1,x2,y2])
    else:
        diagonal_lines.append([x1,y1,x2,y2])
        

    if x2 > maximum_x:
        maximum_x = x2
    if y2 > maximum_y:
        maximum_y = y2

maximum_x += 10
maximum_y += 10

plot = [ [ '.' for x in range(maximum_x) ] for y in range(maximum_y) ]
danger = 0

def modify_plot(y: int, x: int):
    if plot[y][x] == '.':
        plot[y][x] = 1
    else:
        plot[y][x] = plot[y][x] + 1
        if plot[y][x] == 2:
            global danger
            danger += 1

for line in horizontal_lines:
    length = line[2] - line[0]
    for offset in range(abs(length) + 1):
        modify_plot(line[1], line[0] + (offset if length > 0 else -offset))

for line in vertical_lines:
    length = line[3] - line[1]
    for offset in range(abs(length) + 1):
        modify_plot(line[1] + (offset if length > 0 else -offset), line[0])

for line in diagonal_lines:
    x_offset_mod = 1 if line[2] > line[0] else -1
    y_offset_mod = 1 if line[3] > line[1] else -1
    
    while line[0] != line[2] + x_offset_mod:
        modify_plot(line[1], line[0])
        line[0] += x_offset_mod
        line[1] += y_offset_mod

for row in plot:
    for column in row:
        print(column, end="")
    print()

print("dagnger is %d" % danger)
