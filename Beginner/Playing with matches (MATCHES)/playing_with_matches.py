l = [6,2,5,5,4,5,6,3,7,6]

for _ in range(int(input())):
    a,b = map(int,input().split())
    
    ans = a + b
    val = 0
    for i in str(ans):
        val += l[int(i)]
    print(val)