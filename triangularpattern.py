'''Given a number N, print a right triangle consisting of +, |, \, -, and the whitespace character.

Note: use escape character to display \.

Input Format

A single line with one number, N.

Constraints

1 <= N <= 20

Output Format

See sample testcases.

Sample Input 0

5
Sample Output 0

+
| \
|   \
|     \
+-------+
Sample Input 1

2
Sample Output 1

+
+-+
Sample Input 2

1
Sample Output 2

+'''














n=int(input())
if n==1:
    print('+')
if n==2:
    print('+')
    print('+',end='')
    print('-',end='')
    print('+')
if n>2:
    k=1
    print('+')
    for i in range(1,n-1):
        print('|',end='')
        print(' '*(2*k-1),end='')
        print('\\')
        k+=1
    print('+',end='')
    print('-'*(2*k-1),end='')
    print('+')
    
