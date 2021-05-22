from math import gcd

for _ in range(int(input())):
    N,A,B,K = map(int,input().split())
    
    lcm = (A*B) // gcd(A,B)
    count =((N//A) + (N//B)) - (2 * (N// lcm))
    if (count >= K):
        print("Win")
    else:
        print("Lose")
