def check(I,n,q):
    if I == 1:
        h = n//2
        t = n-h
    else:
        t = n//2
        h = n-t
        
    if q == 1:
        return h
    else:
        return t

if __name__=='__main__':
    for _ in range(int(input())):
        g=int(input())
        for _ in range(g):
            (I,n,q)=map(int, input().split())
            res=check(I,n,q)
            print(res)
