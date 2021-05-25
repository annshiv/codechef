for _ in range(int(input())):
    n, k = map(int,input().split())
    lst = list(map(int,input().split()))

    s = ''
    for i in lst:
        if i <= k:
            s += '1'
            k -= i
        else:
            s += '0'
    print(s)