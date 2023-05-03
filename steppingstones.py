import math
T=int(input())
for i in range(T):
    a=int(input())
    n=(math.sqrt(1+8*a)-1)/2 
    if n.is_integer():
        print("Go On Bob {}".format(int(n)))
    else:
        print("Better Luck Next Time")
        
        