s = input()
tree = [None for i in range(1024)]

row = int(input())
for i in range(len(s)):
    ix = 0
    while tree[ix] != None:
        if s[i] < tree[ix]:
            ix = ix*2 + 1
        else:
            ix = ix*2 + 2
    tree[ix] = s[i]
print(*[i for i in tree[max(0, 2**(row-1)-1):min(1024, 2**(row)-1)] if i != None])