for i in range(int(input())):
    n=int(input())
    f=0
    if n>=1:
        for k in range(1,n+1):
           if n%k==0:
             f=f+1
    if f==2:
        print("yes")
    else:
        print("no")