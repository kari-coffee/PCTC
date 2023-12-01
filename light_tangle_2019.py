n = int(input())
c = int(input())
d = {}
count = {}
for _ in range(c):
  a, b = [int(i) for i in input().split()]
  if a in d:
    d[a].append(b)
  else:
    d[a] = [b]
  if b in d:
    d[b].append(a)
  else:
    d[b] = [a]
  if a in count:
    count[a] += 1
  else:
    count[a] = 1
  if b in count:
    count[b] += 1
  else:
    count[b] = 1
ends = []
for i in count:
  if count[i] == 1:
    ends.append([i])
done = set()

for i in ends:
  change = True
  while i[-1] in d and change:
    change = False
    if d[i[-1]] != []:
      if d[i[-1]][0] not in i:
        i.append(d[i[-1]][0])
        change = True
      elif len(d[i[-1]]) == 2:
        i.append(d[i[-1]][1])
        change = True
print(len(max(ends, key=lambda x:len(x))))
