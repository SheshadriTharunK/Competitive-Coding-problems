'''RotationalIndexQuery-I

You are given an integer sequence A of size N. You are also given Q queries which can be one of the following two types:

1 Y - Left circular shift the array Y times.
2 K - Print the element at K th index of A.
Input Format

First line of input contains N and Q.
Second line contains N space separated integers denoting the sequence A.
Each line in next Q lines will have queries of anyone of the two types.
Constraints

1 <= N, Q <= 10^5
0 <= Y,K <= N-1
1 <= A[i] <= 10^9 (0 <= i < N)
Output Format

For each query of type2, output a line with an expected answer.

Sample Input 0

5 6
10 20 30 40 50
1 3
2 0
2 2
1 1
2 1
2 3
Sample Output 0

40
10
10
30

'''
n,q=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(q):
        o,b=map(int,input().split())
        if o==1:
            c+=b 
           
        else:
          if c>len(a)-1:
              c=c%len(a)
          k=(c+b)%len(a)
          print(a[k])




















