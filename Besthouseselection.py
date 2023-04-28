T=int(input())
l=[]
for i in range(T):
    p,b,sqft=map(int,input().split())
    if b>=4 and sqft>=2500 and p<=400000:
        l.append((p,b,sqft))
l.sort(key=lambda x:x[0]//x[2])
if len(l)==1:
    print(*l[0])
elif len(l)>1:
    for i in range(2):
        
           print(*l[i])
else:
    print("You are out of luck, Prof.X.")