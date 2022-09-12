## CodeForces problem 1705B - Mark the Dust Sweeper
## https://codeforces.com/problemset/problem/1705/B

t = int(input())

for c in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    nOfZeros = 0    
    accumulator = 0
    isCountingZeros = False

    for e in a[:-1]:
        if e!=0:
            accumulator+=e
            isCountingZeros = True
        elif isCountingZeros:
            nOfZeros+=1          
        
    if accumulator > 0:
        print(accumulator + nOfZeros)
    else:
        print(0)