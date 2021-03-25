def sums(a,b):
    for i in range(a):
        sums_val = 0
        for j in range(1,b+1):
            sums_val += j
        b = sums_val
    return sums_val

for _ in range(int(input())):
    (a,b) = map(int,input().split())
    print(sums(a,b))