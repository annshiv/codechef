for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    for i in range(2):
        numbers.append(numbers[i])
    curr = sum(numbers[: 3])
    MAX = curr
    for i, num in enumerate(numbers[3 :]):
        curr = curr + num - numbers[i]
        if curr > MAX: 
            MAX = curr
            
    print (MAX)
