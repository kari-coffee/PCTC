grid = [list(input()) for i in range(6)]

for i in range(len(grid)):
    if '#' in grid[i]:
        y = i
        x = grid[i].index('#')
done = set()
done.add((y, x))
origy, origx = y, x
grid[y][x] = '0'
while True:
    change = False
    for dy, dx in [(0,1),(1,0),(-1,0),(0,-1)]:
        ny, nx = (dy+y)%6, (dx+x)%6
        if grid[ny][nx] == '0' and (ny, nx) not in done:
            done.add((ny, nx))
            change = True
            y, x = ny, nx
            break
    if not change:
        grid[y][x] = '#'
        break
for i in grid:
    print(''.join(i))