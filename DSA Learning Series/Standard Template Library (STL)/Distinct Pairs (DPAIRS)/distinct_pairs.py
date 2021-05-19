N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
    
mA = A.index(min(A))
mB = B.index(max(B))
pairs=[]
    
for i in range(M):
    pairs.append((mA,i))
    
for i in range(N):
    if(mA!=i):
        pairs.append((i,mB))
    
for i in pairs:
    print(*i)
