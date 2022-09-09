from math import floor

t = int(input())
for i in range(t):
    intervalo = 24
    n, H, M = [int(c) for c in input().split()]
    time = H + (M/60)
    for j in range(n):
        h, m = [int(c) for c in input().split()]
        tAlarm = h + (m/60)
        if tAlarm < time:
            newInt = tAlarm + (24 - time)
        else:
            newInt = tAlarm - time
        intervalo = min(intervalo, newInt)

    hours = floor(intervalo)
    print(hours, round((intervalo - hours)*60))