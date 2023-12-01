# from collections import deque
# n = int(input())
# s = input()
# d = {i:s[i] for i in range(n)}
# con = {}
# for _ in range(int(input())):
#     a, b = [int(i)-1 for i in input().split()]
#     if a in con:
#         con[a].append(b)
#     else:
#         con[a] = [b]
#     if b in con:
#         con[b].append(a)
#     else:
#         con[b] = [a]

# queue = deque([[0, 0, set()]])
# while queue:
#     cur, dragons, done = queue.popleft()
#     done.add(cur)
#     if d[cur] == 'T':
#         print(dragons)
#         break
#     elif d[cur] == 'D':
#         dragons += 1
#     if cur in con:
#         for i in con[cur]:
#             if i not in done:
#                 queue.append([i, dragons, done])

from collections import deque

INF = 99999
n = int(input())
contents = input()
m = int(input())
connections = []
d = [INF] * n

d[0] = 0
if contents[0] == 'D':
	d[0] += 1

for i in range(n):
	connections.append([])

for i in range(m):
	x, y = map(int, input().split())
	connections[x - 1].append(y - 1)
	connections[y - 1].append(x - 1)

Q = deque()
Q.append(0)
while True:
	cur = Q.popleft()
	if contents[cur] == 'T':
		print(d[cur])
		break
	for vault in connections[cur]:
		if d[vault] == INF:
			if contents[vault] == 'D':
				d[vault] = d[cur] + 1
				Q.append(vault)
			else:
				d[vault] = d[cur]
				Q.appendleft(vault)