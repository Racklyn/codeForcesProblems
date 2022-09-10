t = int(input())
for c in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    menor = min(a)
    maior = max(a)

    juntos = False
    for i in range(n-1):
        if a[i]==maior and a[i+1]==menor:
            juntos = True
            break

    if (menor == a[0] or maior == a[-1] or juntos):
        print(maior - menor)
    else:
        m1 = max(a[1:]) - a[0]
        m2 = a[-1] - min(a[:-1])

        print(max(m1, m2))