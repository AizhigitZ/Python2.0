from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    nl = list(map(int, input().split()))

    count = nl[n-2]
    rr = n-3
    for i in range(rr, -1, -1):
        count -=nl[i]



    print(nl[-1]-count)