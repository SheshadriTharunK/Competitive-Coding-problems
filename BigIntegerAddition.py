n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
rem=0
sum=''
carry2=0
i=len(a)-1
if (m==n):
    while(i!=0):
            carry=carry2+a[i]+b[i]
            rem=carry%10
            carry2=carry//10
            sum+=str(rem)
            i-=1
    carry=carry2+a[i]+b[i]
    sum=str(carry)+sum[::-1]
elif (n>m):
    k=m-1
    for i in range(n-1,-1,-1):
        if k==-1:
            carry=carry2+a[i]
        else:
            carry=carry2+a[i]+b[k]
            rem=carry%10
            carry2=carry//10 
            sum+=str(rem)
            k=k-1
    sum=str(carry)+sum[::-1]
elif (m>n):
    m,n=n,m
    a,b=b,a
    k=m-1
    for i in range(n-1,-1,-1):
        if k==-1:
            carry=carry2+a[i]
        else:
            carry=carry2+a[i]+b[k]
            rem=carry%10
            carry2=carry//10 
            sum+=str(rem)
            k=k-1
    sum=str(carry)+sum[::-1]
for i in sum:
    print(i,end=' ')
    
    
    