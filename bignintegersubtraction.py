n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum=''
i=n-1
s=n-1
if (m==n):
    while(i!=0):
            carry=a[i]-b[i]
            i-=1
            sum+=str(carry)
    carry=a[i]-b[i]
    sum=str(carry)+sum[::-1]

elif(a[s]==0):
    s1=''.join(map(str,a))
    s2=''.join(map(str,b))
    sum=str(int(s1)-int(s2))
elif (a[n-1]<b[m-1]):
    s1=''.join(map(str,a))
    s2=''.join(map(str,b))
    sum=str(int(s1)-int(s2))

else:
    k=m-1
    for i in range(n-1,-1,-1):
            if k==-1:
                carry=a[:n-m]
                s=''.join(map(str,carry))
            else:
                carry=a[i]-b[k]
                sum+=str(carry)
                k=k-1
    sum=str(s)+sum[::-1]
for i in sum:
    print(i,end=' ')
    
    
    