s = input()
ans = ''
stack = []
for i in s:
    if i == '[':
        stack.append([])
    elif i == ']':
        x = stack.pop()
        ans += str((x[0]+x[-1])//2)
    elif i.isdigit():
        stack[-1].append(int(i))
print(ans)