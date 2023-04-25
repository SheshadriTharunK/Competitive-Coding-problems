cipher = input().upper()
secret = input().upper()
k11='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message=''
i=0
for i in range(len(secret)):
    
         message+=chr((ord(cipher[i])-ord(secret[i]))%26+65)
    
key=secret+message
message=''
k=0
for i in range(len(cipher)):
    if cipher[i] in k11:
       message+=chr((ord(cipher[i])-ord(key[k]))%26+65)
    else:
        message+=secret[i]
    k+=1 
    if k==len(secret):
        k=0 
        key=message[-len(secret):]
print(message)

