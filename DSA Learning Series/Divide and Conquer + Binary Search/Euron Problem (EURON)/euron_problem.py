from bisect import bisect

n  = int(input())
l = list(map(int, input().split()))
i, ans = 1 ,0
while i < n:
    if l[i] < l[i-1]:
        ind = bisect(l ,l[i], 0, i-1)
        ans += i - ind
        temp = l.pop(i)
        l.insert(ind , temp )
    i+=1
print(ans)
