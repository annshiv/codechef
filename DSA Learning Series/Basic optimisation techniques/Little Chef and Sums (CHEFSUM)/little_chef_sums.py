for _ in range(int(input())):
    n=int(input())
    nums=list(map(int, input().split()))
    
    ini=10**5
    for i in range(n):
        if ini>nums[i]:
            ini=nums[i]
            res=i
        
    print(res+1)
