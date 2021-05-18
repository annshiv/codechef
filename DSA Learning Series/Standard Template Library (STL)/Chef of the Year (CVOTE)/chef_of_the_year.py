n,m=map(int,input().split())
d,d1,d2={},{},{}
for i in range(n):
    a,b=input().split()
    d[a]=b
for i in d:
    d1[i]=0
    d2[d[i]]=0
for i in range(m):
    a=input()
    d1[a]+=1
    d2[d[a]]+=1
m=max(d2.values())
l=[]
for i,j in d2.items():
    if j==m:
        l.append(i)
print(sorted(l)[0])
m=max(d1.values())
l=[]
for i,j in d1.items():
    if j==m:
        l.append(i)
print(sorted(l)[0])
