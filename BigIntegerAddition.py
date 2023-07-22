'''BigIntegerAddition

Given two numbers X and Y, each has N and M decimal digits respectively, you need to compute the digits after adding X and Y. Assume that most significant digit of each number is at left most side.

Input Format

The first line contains N and M.

The second line contains N digits, separated by spaces, for X.

The third line contains M digits, separated by spaces, for Y.

No leading zeros are available in X and Y.

Constraints

1 <= N,M <= 10^4

Each digit is between 0 and 9, inclusive

Output Format

Output a line that consists of the decimal digits representing X + Y. Keep a space between digits.

Sample Input 0

3 3
1 2 3
4 5 6
Sample Output 0

5 7 9
Sample Input 1

1 1
4 
6
Sample Output 1

1 0

​'''
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
    
    
    
