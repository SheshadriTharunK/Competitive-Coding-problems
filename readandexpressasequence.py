n=int(input())
s=input()
for i in range(n):
    count=1 
    prev=s[0]
    new_s=''
    for j in range(1,len(s)):
        if s[j]==prev:
            count+=1 
        else:
            new_s+=str(count)+prev
            count=1 
            prev=s[j]
    new_s+=str(count)+prev
    s=new_s 
print(s)