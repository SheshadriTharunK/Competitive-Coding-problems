s=input()
k=len(s)-len(str(len(s)))
ans=''
for i in range(k):
    ans+=s[i]
print(ans)
    