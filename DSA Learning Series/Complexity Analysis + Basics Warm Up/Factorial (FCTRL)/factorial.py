for _ in range (int(input())):
    n = int(input())
    
    c=0
    while (n>=5):
        n//=5
        c+=n
    
    print(c)
