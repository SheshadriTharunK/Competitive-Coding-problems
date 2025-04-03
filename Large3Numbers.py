a=[-5,-4,-3,-2,-1]
n1=float('-inf')
n2=float('-inf')
n3=float('-inf')
for i in a:
    if i>n1:
        n3=n2
        n2=n1
        n1=i 
    elif i>n2:
        n3=n2
        n2=i 
    elif i>n3:
        n3=i
print(n1,n2,n3)
