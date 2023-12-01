# #set - 4/10
# n = int(input())
# arr = []
# for _ in range(n):
#     x, y, w, h = [int(i) for i in input().split()]
#     z = set()
#     for row in range(y, y+h):
#         for col in range(x, w+x):
#             z.add((row, col))
#     arr.append(z)
# print(len(arr[0].intersection(*arr)))

# #dict - 5/10
# n = int(input())
# arr = []
# for _ in range(n):
#     x, y, w, h = [int(i) for i in input().split()]
#     arr.append([x,y,w,h])
# d = {}
# for x, y, w, h in arr:
#     for row in range(y, y+h):
#         for col in range(x, x+w):
#             if (row,col) in d:
#                 d[(row,col)] += 1
#             else:
#                 d[(row,col)] = 1
# ans = list(d.values()).count(n)
# print(ans)

#intervals - 10/10
n = int(input())
starts_x = 0
ends_x = 10000000000000
starts_y = 0
ends_y = 10000000000000
for _ in range(n):
    x, y, w, h = [int(i) for i in input().split()]
    starts_x = max(x, starts_x)
    starts_y= max(y, starts_y)
    ends_x = min(x+w, ends_x)
    ends_y = min(y+h, ends_y)
print((starts_x-ends_x)*(starts_y-ends_y))