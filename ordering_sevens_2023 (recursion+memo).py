n = int(input())

d = {}
def solve(n):
    if n in d:
        return d[n]
    
    if n < 10:
        if n >= 7:
            return 1
        else:
            return 0
        
    s = str(n)
    add = 0
    if s[0] == '7':
        add = int(s[1:])+1
    elif int(s[0]) > 7:
        add = 10**(len(s)-1)

    d[n] = solve(int('9'*(len(s)-1)))*int(s[0]) + solve(int(s[1:])) + add
    return d[n]
print(solve(n))
