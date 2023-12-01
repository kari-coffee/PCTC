from math import sqrt
d = int(input())
n = int(input())
beacons = []
a = [(0,0)]
for _ in range(n):
    beacons.append([int(i) for i in input().split()])
lit = 0
last = lit

def dist(i, j):
    return sqrt((abs(j[0]-i[0]))**2 + (abs(j[1]-i[1]))**2)

while True:
    valid = False
    length = len(a)
    for j in range(length):
        count = 0
        while beacons and count < len(beacons):
            if dist(beacons[count], a[j]) <= d:
                a.append(beacons.pop(count))
                lit += 1
            else:
                count += 1
    a = a[length:]
    if lit == last:
        break
    else:
        last = lit
    print(lit)
    