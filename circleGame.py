## Codeforces problem Circle Game https://codeforces.com/problemset/problem/1695/B
## Solved by Racklyn

t = int(input())

for c in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    if n % 2 == 1:
        print("Mike")
    else:
        # Searching index of smallest pile (first found)
        idxSmall = 0
        small = 10**9 + 1
        for i, s in enumerate(a):
            if s < small:
                small = s
                idxSmall = i
        print(["Joe", "Mike"][idxSmall % 2]) # Wins how has not taken the first smallest