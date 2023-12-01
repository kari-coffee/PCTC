n = int(input())
d = {}
from collections import deque
for i in range(1, n+1):
    x = int(input())
    d[i] = x
num = 0
ans = 0
queue = deque([[i, set()] for i in range(1,n+1)])
while queue:
    cur, done = queue.popleft()
    if cur in d:
        if d[cur] in done:
            done.add(cur)
            if (length := len(done)) > ans:
                ans = len(done)
                num = 1
            elif length == ans:
                num += 1
        else:
            done.add(cur)
            queue.append((d[cur], done))
print(ans)
print(num)
