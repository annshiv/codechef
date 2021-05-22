for _ in range(int(input())):
    k, q = map(int, input().split())
    mot = sorted(list(map(int, input().split())))
    sat = sorted(list(map(int, input().split())))
    qs = []
    for i in range(q):
        qs.append(int(input()))
    
    gen = [mot[i]+sat[j] for i in range(k) for j in range(min(k, 10001//(i+1)))]
    gen.sort()

    res = [gen[e-1] for e in qs]

    print(*res)
