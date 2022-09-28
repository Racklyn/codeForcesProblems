## Codeforces problem 1593/C - Save More Mice https://codeforces.com/problemset/problem/1593/C
## Solved by Racklyn, Lucas and Jucyelle

t = int(input())

miceDistance = []

for i in range(t):
    n, k = [int(i) for i in input().split()]
    miceDistance = [ n - int(i) for i in input().split()]

    miceDistance.sort()

    catDistance = n - 1

    c = 0
    savedMice = 0
    for i,m in enumerate(miceDistance):
        c += m

        if c > catDistance:
            break
        savedMice+=1

    print(savedMice)
    



