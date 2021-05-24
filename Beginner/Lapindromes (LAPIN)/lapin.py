for _ in range(int(input())):
    s = input()
    if len(s) % 2 != 0:
        split = len(s)//2
        a = s[:split]
        b = s[split+1:]

    else:
        split = len(s)//2
        a = s[:split]
        b = s[split:]

    ans = None
    a_list = [x for x in a]
    a_list.sort()
    b_list = [x for x in b]
    b_list.sort()

    if a_list == b_list:
        print('YES')
    else:
        print('NO')