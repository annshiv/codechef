for _ in range(int(input())):
    n=int(input())
    sl=list(map(int, input().split()))
    prev=sl[0]
    c=0
    for i in range(n):
        curr=min(prev,sl[i])
        c+=1 if curr==sl[i] else 0
        prev=curr
    print(c)
