w,b = input().split()              
w = int(w)                        
b = float(b)                            
if (w % 5 == 0 and b>=(w+0.5)):
    b = (b - w) - 0.5     
    print('%.2f' % b)
else:
    print('%.2f' % b)
    
    
#in a different style
withdraw, bal = map(float,  input().split() )

if withdraw%5==0 and withdraw+0.50<=bal:
    bal-= (withdraw+0.50)
print(bal)
