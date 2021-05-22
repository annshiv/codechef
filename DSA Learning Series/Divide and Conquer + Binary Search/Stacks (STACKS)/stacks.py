def bSearch(ind,val,l,r):
    ans = ind
    while r>=l:
        m = (r+l)//2
        if s[m]>val:
            ans = m; r = m-1
        else:
            l = m+1
    return ans
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = []; size = 1
    s.append(a[0])
    for i in range(1,n):
        if a[i]>=s[-1]:
            s.append(a[i]); size += 1
        else:
            index = bSearch(i,a[i],0,size-1)
            s[index] = a[i]
            
    print(size,*s)
