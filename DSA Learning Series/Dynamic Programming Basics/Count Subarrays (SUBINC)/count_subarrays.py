for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=1
    i=1
    count=0
    while i<n:

       if  l[i]<l[i-1]:
           count+=(c*(c+1))//2
           c=1
       else:
           c+=1
       i+=1
    count+=(c*(c+1))//2
    print(count)
