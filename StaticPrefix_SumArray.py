'''StaticPrefixSumQuery

Given an integer sequence A of size N, you are asked to perform Q queries which are of the following type:

K - Find sum of all the elements from index 0 to index K of A.
Input Format

First line of input contains N and Q.
Second line contains N space separated integers denoting the sequence A.
Each line in next Q lines will have queries of the given type.
Constraints

1 <= N, Q <= 10^5
0 <= K <= N-1
-10^9 <= A[i] <= 10^9 (0 <= i < N)
Output Format

For each query, output a line with expected answer.

Sample Input 0

6 3
-2 0 3 -5 2 -1
2
5
3
Sample Output 0

1
-3
-4'''
n,q=map(int,input().split())
a=list(map(int,input().split())) 
for i in range(1,len(a)):
    a[i]=a[i]+a[i-1]
for i in range(q):
       k=int(input())
       print(a[k])
