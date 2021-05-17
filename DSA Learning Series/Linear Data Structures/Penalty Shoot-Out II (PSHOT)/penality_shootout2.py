for _ in range(int(input())):
    
    n=int(input())
    goal=input()
    team_1=team_2=0
    a=b=n
    for i in range(2*n):
        if i%2==0:
            a-=1
            if goal[i]=='1':team_1+=1      
        else :
            b-=1
            if goal[i]=='1':team_2+=1

        if team_1>team_2: 
            if team_1>team_2+b:
                print(i+1)
                break
        elif team_2>team_1:
            if team_2>team_1+a:
                print(i+1)    
                break       
    if team_1==team_2:
        print(n*2)
