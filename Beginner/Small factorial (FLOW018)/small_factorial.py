
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

for _ in range(int(input())):
    n = int(input())
    print(fact(n))

    
#same approach without function
for _ in range(int(input())):
    fact=[]
    res=1
    for num in range(1,int(input())+1):
        res *= num
    print(res)
