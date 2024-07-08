s='[a][b][c]'
k=0
s2=''
m=''
for i in s:
    if i.isdigit():
       k=k*10+int(i)
    elif i=='[':
       s1=''
    elif i==']':
        s2+=s1*k 
        k=0
        s1=''
    else:
        s1+=i 
        m+=i 
if len(m)<len(s2+s1):
     print(s1+s1) 
else:
    print(m)
        
