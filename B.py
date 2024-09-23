from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n, k = map(int, input().split())

    if k % 2 == 0 and k//2>1 and (k//2)%2 ==0:
        print("YES")
    elif  n % 2 == 1 and k % 2 == 1 and (k//2)%2 ==1:
        print("YES")
    elif n % 2 == 0 and k % 2 == 1 and (k//2)%2 ==0:
        print("YES")
    else:
        print("NO")