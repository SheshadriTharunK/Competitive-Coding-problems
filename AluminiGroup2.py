'''AlumniGroup-II
You need to write a simple program for tracking students of an alumni-group using their unique IDs. Students can either enter or exit the group at anytime. If queried then your program should respond with the number of active users in the group at the query time. You can assume that only students existing in the group only perform exit operation and also students outside the group only perform enter operation. Intially, all the students are outside the group.

Input Format

First line consists of a number n, indicating the total number of operations.

This is followed by n lines, each line describing either an entry or exit or query operation. Each description is of the form 'entry ID' or 'exit ID' or 'query'.

Constraints

1 <= n <= 10^6
Length of each ID is 10
ID consists of lowercase characters only
Output Format

Each query must respond with a line containing the size of the group till that time.

Sample Input 0

8
entry krishna
query
exit krishna
entry sitara
entry raj
query
entry nakshatra
query
Sample Output 0

1
2
3
Sample Input 1

10
entry krishna
query
exit krishna
query
entry sitara
query
entry raj
query
entry nakshatra
query
Sample Output 1

1
0
1
2
3'''
T=int(input())
count=0
for i in range(T):
    a=input().split()
    if a[0]=='query':
        print(count)
    elif a[0]=='entry':
        count+=1 
    else:
        count-=1
    