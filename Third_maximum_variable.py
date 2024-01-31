a=[9,8,7,6,5,4,32]
m1=float('-inf')
m2=float('-inf')
m3=float('-inf')
for i in a:
    if i>m1:
        m3=m2
        m2=m1
        m1=i 
    elif i>m2:
        m2=i
    elif i>m3:
        m3=i
print(m1,m2,m3)
