T=int(input())
r='hackerrank'

for i in range(T):
    index=0
    x=input()
    for i in x:
        if i==r[index]:
            index=index+1 
        if index==len(r):
            print('YES')
            break
    else:
            print('NO')
    
