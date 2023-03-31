n = int(input())
t = int(input())
d = []
for _ in range(t):
    a, b, st, en = input().split()
    a = int(a)
    b = int(b)
    st = int(st[:2])*60+int(st[3:])
    en = int(en[:2])*60+int(en[3:])
    if st >= 5*60:
        d.append([a, b, st ,en])
d.sort()
dp = [99999 for i in range(n+1)]
dp[1] = 4*60+57
for i in d:
    a, b, st, en = i
    if dp[a] <= st-3:
        dp[b] = min(dp[b], en)
shortest = dp[n]
hours = str(shortest // 60)
shortest %= 60
shortest = str(shortest)
if len(shortest) == 1:
    shortest = '0'+shortest
if len(hours) == 1:
    hours = '0'+hours
print(f"{hours}:{shortest}")
