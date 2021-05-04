N = int(input())
c=1
res=[]
for i  in range (1,int((N+2)/2)):
    if N%i == 0:
        res.append(i)
        c+=1
res.append(N)
print(c)
print(*res)
