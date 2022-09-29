map_list = []
for line in open("milk"):
    map_list.append([int(part) for part in line.split(",")])

m = 0

for i in range(len(map_list)):
    for j in range(i + 1, len(map_list)):
        m = max(m,
                abs(map_list[i][0] - map_list[j][0]) + \
                abs(map_list[i][1] - map_list[j][1]) + \
                abs(map_list[i][2] - map_list[j][2]))
print(m)
