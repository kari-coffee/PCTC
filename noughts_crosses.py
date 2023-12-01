grid = [[-1 for i in range(4)]for j in range(4)]
p1 = 0
p2 = 0
d = {'a':0,'b':1,'c':2,'d':3}
for i in range(16):
    x, y = list(input())
    y = 4-int(y)
    x = d[x]
    if i%2 == 0:
        grid[y][x] = 0
    else:
        grid[y][x] = 1

for y in range(4):
    nought = 0
    cross = 0
    for x in range(4):
        if grid[y][x] == 0:
            nought += 1
            cross = 0
        else:
            nought = 0
            cross += 1
        if nought >= 3:
            p1 += 1
        elif cross >= 3:
            p2 += 1
for y in range(4):
    nought = 0
    cross = 0
    for x in range(4):
        if grid[x][y] == 0:
            nought += 1
            cross = 0
        else:
            nought = 0
            cross += 1
        if nought >= 3:
            p1 += 1
        elif cross >= 3:
            p2 += 1
for coords in [[(0,0),(1,1),(2,2),(3,3)],[(0,1),(1,2),(2,3)], [(1,0),(2,1),(3,2)], [(2,0),(1,1),(0,2)], [(3,0),(2,1),(1,2),(0,3)],[(3,1),(2,2),(1,3)]]:
    nought = 0
    cross = 0
    for x, y in coords:
        if grid[y][x] == 0:
            nought += 1
            cross = 0
        else:
            cross += 1
            nought = 0
        if nought >= 3:
            p1 += 1
        elif cross >= 3:
            p2 += 1
print(f"{p1}-{p2}")