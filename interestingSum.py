t = int(input())
res = []
for i in range(t):
    n = int(input())
    a = [int (x) for x in input().split()]

    a.sort()
    min1, min2 = a[:2]
    max1, max2 = a[-2:]

    res.append(max1+max2-min1-min2)

for j in res:
    print(j)