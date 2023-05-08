n=int(input())
L=list(map(int,input().split()))
while(n>1):
    a=L[0]
    b=L[1]
    del L[1]
    n=n-1
    L[0]=a+b+a*b 
    
print(L[0]%1000000007)







