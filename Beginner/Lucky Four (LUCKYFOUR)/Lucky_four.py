for _ in range(int(input())):
    count = 0
    n = input()
    for i in n:
        if i == '4':
            count += 1
    print(count)