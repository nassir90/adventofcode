total = 0
max_x = 292
min_x = 269
min_y = -68
max_y = -44
#min_x = 20
#max_x = 30
#min_y = -10
#max_y = -5
for x in range(max_x + 1):
    for y in range(min_y, -min_y):
        px = 0
        py = 0
        vx = x
        vy = y
        while px <= max_x and py >= min_y:
            px += vx
            py += vy
            vy -= 1
            if vx != 0: vx -= 1
            if px >= min_x and px <= max_x and py <= max_y and py >= min_y:
                total += 1
                break

print(total)
