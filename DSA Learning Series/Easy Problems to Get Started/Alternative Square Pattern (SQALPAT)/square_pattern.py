n = int(input())
for i in range(1,n+1):
    start=(i*5)-4
    lst=[e for e in range(start,start+5)]
    if i%2==1:
        print(*lst)
    if i%2==0:
        lst.reverse()
        print(*lst)
            
