from math import inf

s = input()
v = [ord(letter)-ord('A')-12 for letter in s]

max_so_far = -inf
max_ending_here = 0
ans = [s[0], s[0]]
reset = False

for i, x in enumerate(v):
    max_ending_here += x
    if max_ending_here > max_so_far:
        max_so_far = max_ending_here
        ans[1] = s[i]
    if max_ending_here < 0: # restart 
        max_ending_here = 0
print(max_so_far)
print(''.join(ans))
