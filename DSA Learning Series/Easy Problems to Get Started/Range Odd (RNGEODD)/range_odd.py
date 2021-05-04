L,R=map(int, input().split())
odds=[]
for i in range(L,R+1):
    if i%2==1:
        odds.append(i)
print(*odds)
