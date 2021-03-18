lst = []
n = int(input())
for _ in range(n):
    a = input()
    while int(a) % 10 == 0:
        a = int(a) // 10
    a = str(a)
    lst.append(a[::-1])
for j in lst:
    print(j)