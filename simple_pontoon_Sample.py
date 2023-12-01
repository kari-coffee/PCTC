
# d = {'T':10, 'J':10,'Q':10,'K':10, 'A':11}
# s = [d[i] if i in d else int(i) for i in input()]
# n = int(input())
# for r in range(n):
#     hand = [s.pop(0), s.pop(0)]
#     stick = False
#     while not stick:
#         x = sum(hand)
#         if x > 21:
#             ans = 'D'
#             break
#         elif x == 21 and len(hand) == 2:
#             ans = 'A'
#             break
#         elif x <= 21 and len(hand) == 5:
#             ans = 'B'
#             break
#         elif 17 <= x <= 21:
#             ans = f"C{x:02d}"
#             break
#         else:
#             hand.append(s.pop(0))
# print(ans)


d = {'T':10, 'J':10,'Q':10,'K':10, 'A':11}
s = [d[i] if i in d else int(i) for i in input()]
n = int(input())
for r in range(n):
    hand = [s.pop(0), s.pop(0)]
    while True:
        x = sum(hand)
        if x > 21:
            ans = 'D'
            break
        elif x == 21 and len(hand) == 2:
            ans = 'A'
            break
        elif x <= 21 and len(hand) == 5:
            ans = 'B'
            break
        elif 17 <= x <= 21:
            ans = f"C{x:02d}"
            break
        else:
            hand.append(s.pop(0))
print(ans)
