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


# without function
for _ in range(int(input())):
    D,N = map (int, input().split())
    for i in range(D):
        sum=N*(N+1)//2
        N=sum
    print(sum)
