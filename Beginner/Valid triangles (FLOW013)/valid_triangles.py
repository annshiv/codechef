for _ in range(int(input())):
    lst = list(map(int,input().split()))
    if sum(lst) == 180:
        print('YES')
    else:
        print('NO')