for n in range(int(input())):
    num = int(input())
    if num%10 == 0:
        print("0")
    elif num%5 == 0:
        print("1")
    else:
        print("-1")