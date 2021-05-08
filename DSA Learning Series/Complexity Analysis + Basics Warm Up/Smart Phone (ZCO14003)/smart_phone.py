n=int(input())
arr=[int(input()) for _ in range(n)]
s=0
arr.sort()
for i in range(n):
    s=max(s,arr[i]*(n-i))
print(s)
