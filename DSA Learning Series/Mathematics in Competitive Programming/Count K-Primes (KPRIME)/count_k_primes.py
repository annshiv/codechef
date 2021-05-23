MAX = 100000 +1 
sieve = [0]*MAX 
sieve[0],sieve[1] = 0,0
for i in range(2,MAX):
 if sieve[i]==0:
  for j in range(i,MAX,i):
   sieve[j]+=1 

m = [[0 for j in range(MAX)] for i in range(5+1)]
for i in range(1,6):
 for j in range(1,MAX):
  if sieve[j]==i:
   m[i][j] = 1 
  m[i][j]+=m[i][j-1]
  
   
for _ in range(int(input())):
 a,b,k = map(int,input().split())
 res = m[k][b] - m[k][a-1]
 print(res)
 
