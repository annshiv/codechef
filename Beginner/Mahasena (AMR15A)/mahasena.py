n = int(input())
a = list(map(int,input().split()))
odd ,even = 0,0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if (odd == even) or odd > even:
    print('NOT READY')
else:
    print('READY FOR BATTLE')