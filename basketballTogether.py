## Codeforces problem B. Basketball Together - https://codeforces.com/problemset/problem/1725/B
## Solved by Racklyn and Lucas

from math import ceil

n, d = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]

l.sort()
start, final = -1, n-1
times = 0
while(start < final):
    m = ceil(d/l[final])-1
    start += m
    if(l[final]*(m+1) == d):
        start += 1
    if(start >= final):
        break

    times +=1
    final -=1    

print(times)