for i in range(int(input())) :
    a, b = map(int,input().split())
    prod = a * b
    while a%b != 0 :
        z = a % b
        a = b
        b = z
    print(b, prod//b)