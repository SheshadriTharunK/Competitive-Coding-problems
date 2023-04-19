s=input()
n=int(input())
plain=''
p=1
for i in s:
    if i.isupper():
        plain+=chr((ord(i)-p-65)%26+65)

       
    elif i.islower():
        plain+=chr((ord(i)-p-97)%26+97)
   
       
    else:
        plain+=i
    p+=1 
    if p==n+1:
            p=1
    
    
    
    
    
print(plain)