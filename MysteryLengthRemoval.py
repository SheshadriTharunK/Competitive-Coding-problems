s=input()
output=''
k=len(s)-len(str(len(s)))
if len(s)==10:
    for i in range(k+1):
        output+=s[i]
else:
    for i in range(k):
        output+=s[i]
print(output)
