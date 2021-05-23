for _ in range(int(input())):
    n = int(input())
    a = input()
    lst = []
    for i in a:
        lst.append(i)
    
    if 'I' in lst:
        print('INDIAN')
    elif 'Y' in lst:
        print('NOT INDIAN')
    else:
        print('NOT SURE')