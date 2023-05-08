T=int(input())
for i in range(T):
    p=1 
    a=int(input())
    l=list(map(int,input().split()))
    for i in l:
        p=p*i
    print(p%1234567)