a=input()
s={}
for i in range(len(a)):
    if a[i] in s:
        s[a[i]]+=1 
    else:
        s[a[i]]=1
for i in range(len(a)):
    if s[a[i]]==1:
        print(a.rfind(a[i]))
        exit()
else:
    print(-1)