r = []
t = int(input())
for c in range(t):
    a, b = input()
    c, d = input()
    img = {a, b, c, d}
    r.append(len(img) - 1)
for v in r:
    print(v)