def gcd(l,b):
    if(l==0):
        return b
    if(b==0 or l==b):
        return l
    if(l>b):
        return gcd(l-b, b)
    return gcd(l, b-l)

for _ in range(int(input())):
    l,b=map(int, input().split())
    
    print(gcd(l,b))
    
    
