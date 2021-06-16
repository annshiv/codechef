for _ in range(int(input())):
    n,m,c=map(int,input().split())
    d = abs(m-n)
    s = d - c
    if s <= 0:
        print(0)
    else:
        print(s)  