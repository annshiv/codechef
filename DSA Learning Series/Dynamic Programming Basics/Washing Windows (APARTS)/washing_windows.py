t=int(input())

for i in range(t):
    nm=list(map(int, input().split()))
    n=nm[0]
    m=nm[1]
    
    
    
    mat=[[0]*(m+2)]
    mx=[[0]*(m+2)]
    for i in range(n):
            temp=list(map(int,input().split()))
            temp=[0]+temp+[0]
            mat+=[temp]
            mx+=[temp]
    mat+=[[0]*(m+2)]
    mx+=[[0]*(m+2)]
    
  
    
    for i in range(1,n+1):
        final=""
        for j in range(1,m+1):
            if mat[i][j]>max(mx[i-1][j-1], mx[i-1][j],mx[i-1][j+1]):
                final+="1"
                mx[i][j]=mat[i][j]
            else:
                final+="0"
                mx[i][j]=max(mx[i-1][j-1], mx[i-1][j],mx[i-1][j+1])
        print(final)
