from sys import stdin 

t = int(stdin.readline())

for _ in range(t):
    n, k = map(int, input().split())

    nl = list(map(int, input().split()))
    total = 0
    count = 0
    for i in nl:
        if i >= k:
            total += i
        elif (i == 0) and (total > 0):
            total -=1
            count += 1

    print(count)
