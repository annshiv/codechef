for _ in range(int(input())):
        inp=int(input())
        a = [int(n) for n in input().split()]
        s=0 
        mi=10**9
        for i in a:
            mi=min(mi,i)
            s+=mi
        print(s)
