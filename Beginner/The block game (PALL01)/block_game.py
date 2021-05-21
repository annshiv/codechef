for _ in range(int(input())):
    a = input()
    if a[::-1] == a :
        print('wins')
    else:
        print('loses')