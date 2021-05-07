a,b,c=map(int, input().split())

if a+b>c and b+c>a and a+b >c:
    if a == b == c:
        print(1)
    elif a==b or b==c or a==c:
        print(2)
    else:
        print(3)
else:
    print(-1)
