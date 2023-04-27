T=int(input())
for i in range(T):
    x=input()
    l=[]
    count=0 
    for i in x:
        if i not in l:
            count+=1 
            l.append(i)
    print(count)s