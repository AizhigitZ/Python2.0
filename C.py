from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    nls = sorted(list(map(int, input().split())))

    middle = nls[n//2]

    needed = int(middle*n*2+1)

    summ = sum(nls)

    if n == 1 or (n == 2):
        print(-1)

    elif needed <=summ:
        print(0)

    else:
        print(needed-summ)


    



        

    
