
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

for _ in range(int(input())):
    n = int(input())
    print(fact(n))
