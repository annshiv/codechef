lst=list(map(int, input().split()))
if sum(lst)==180 and 0 not in lst:
    print('YES')
else:
    print('NO')
