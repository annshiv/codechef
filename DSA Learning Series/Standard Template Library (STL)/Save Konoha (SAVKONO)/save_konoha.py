from heapq import heappop, heappush, heapify 

for _ in range(int(input())):
    N, Z = map(int, input().split())
    A = list(map(int, input().split()))
    A = [-1*x for x in A]
    heapify(A)
    c = 0
    while N != 0 and Z > 0:
        x = -1 * heappop(A)
        Z -= x
        x = x // 2
        if x > 0:
            heappush(A, -1 * x)
        c += 1
    if Z > 0: 
        print("Evacuate")
    else: 
        print(c)
