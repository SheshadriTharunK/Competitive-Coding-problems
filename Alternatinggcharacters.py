T=int(input())
for i in range(T):
    s=input()
    count=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
    print(count)
