T=int(input())
for _ in range(T):
    N=int(input())
    profs=[]
    for i in range(N):
        s,p,v=map(int,input().split())
        res=(p//(s+1))*v
        profs.append(res)
    print(max(profs))
