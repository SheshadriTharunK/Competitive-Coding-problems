''''''
BigIntegerSubtraction

GGiven two numbers X and Y, each has N and M decimal digits respectively, you need to compute the digits after subtracting Y from X. Assume that most significant digit of each number is at left most side.

Input Format

The first line contains N and M.

The second line contains N digits, separated by spaces, for X.

The third line contains M digits, separated by spaces, for Y.

No leading zeros are available in X and Y.

Constraints

1 <= N,M <= 10^4

Each digit is between 0 and 9, inclusive

X >= Y and N >= M

Output Format

Output a line that consists of the decimal digits representing X - Y. Keep a space between digits.

Sample Input 0

3 3
4 5 6
1 2 3
Sample Output 0

3 3 3
​'''

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum=''
i=n-1
s=n-1







if (m==n)and (a[n-1]<b[m-1]):
    s1=''.join(map(str,a))
    s2=''.join(map(str,b))
    sum=str(int(s1)-int(s2))
elif (m==n):
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
    
    
    

​'''

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum=''
i=n-1
s=n-1







if (m==n)and (a[n-1]<b[m-1]):
    s1=''.join(map(str,a))
    s2=''.join(map(str,b))
    sum=str(int(s1)-int(s2))
elif (m==n):
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
    
    
    
