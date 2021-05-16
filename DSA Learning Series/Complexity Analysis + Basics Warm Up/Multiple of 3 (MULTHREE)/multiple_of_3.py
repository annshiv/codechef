for _ in range(int(input())):
    k,d0,d1 = map(int,input().split())
    if(k==2):
        t = d0+d1
    else:
        s = str(d0)+str(d1)
        s=s+str((d0+d1)%10)
        m1 = d0+d1+(d0+d1)%10
        l=[int(s[0]),int(s[1]),int(s[2])]
        s1 = ''
        n = 1
        m2=0
        while(n<=4):
            n+=1
            c1 = sum(l)%10
            m2+=c1
            s1=s1+(str(c1))
            l.append(c1)
            
        n1 = k-3
        if(n1//4==0):
            m4 = s1[0:n1]
            m3=0
            for i in m4:
                m3+=int(i)
            t = m1+m3
        else:
            n2 = n1-n1//4
            if(n2==0):
                t = m1+m2*(n1//4) 
            else:
                m4 = s1[0:(n1-4*(n1//4))]
                m3=0
                for i in m4:
                    m3+=int(i)
                t=m1+m2*(n1//4)+m3
    #print(t)
    if(t%3==0):
        print('YES')
    else:
        print('NO')
