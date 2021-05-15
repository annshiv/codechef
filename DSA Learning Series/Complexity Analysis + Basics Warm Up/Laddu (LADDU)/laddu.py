for cas in range(int(input())):
    n, origin = input().strip().split()
    points = 0
    for i in range(int(n)):
        data = input().strip().split()
        kind = data[0]
        if kind == 'CONTEST_WON':
            rank = int(data[1])
            bonus = max(0, 20 - rank)
            points += 300 + bonus
        elif kind == 'TOP_CONTRIBUTOR':
            points += 300
        elif kind == 'BUG_FOUND':
            severity = int(data[1])
            points += severity
        elif kind == 'CONTEST_HOSTED':
            points += 50

    print (points // (200 if origin == 'INDIAN' else 400))
