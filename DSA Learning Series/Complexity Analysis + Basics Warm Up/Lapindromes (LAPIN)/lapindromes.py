for _ in range(int(input())):
    s=input()
    l=len(s)
    h=l//2
    
    l1=list(s[:h])
    l1.sort()
    if l%2==0:
        l2=list(s[h:])
        l2.sort()
    else:
        l2=list(s[h+1:])
        l2.sort()

    if l1==l2:
        print('YES')
    else:
        print('NO')
