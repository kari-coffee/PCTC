n = int(input())
t = int(input())
d = {}
for _ in range(t):
    a, b, st, en = input().split()
    a = int(a)
    b = int(b)
    st = int(st[:2])*60+int(st[3:])
    en = int(en[:2])*60+int(en[3:])
    if st >= 5*60:
        if a in d:
            d[a].append([b, st, en])
        else:
            d[a] = [[b, st, en]]

queue = [[1, 5*60]]
shortest = 100000000
while queue:
    cur, time = queue.pop(0)
    if time > shortest:
        continue
    if cur == n:
        shortest = min(shortest, time)
        continue
    time += 3
    if cur in d:
        for c in d[cur]:
            if c[1] >= time and c[2] < shortest:
                queue.append([c[0], c[2]])
hours = str(shortest // 60)
shortest %= 60
shortest = str(shortest)
if len(shortest) == 1:
    shortest = '0'+shortest
if len(hours) == 1:
    hours = '0'+hours
print(f"{hours}:{shortest}")
