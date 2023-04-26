cipher=input().upper()
secret=input().upper()
key=secret 
tmp=''
res=''
for i in range(len(cipher)):
    tmp=chr((ord(cipher[i])-ord(key[i]))%26+65)
    res+=tmp
    key+=tmp 
print(res)