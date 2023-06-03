'''
A special sheep species called kilkili is discovered in a remote village of india. The number of sheeps having same height in kilkili group is always even except one. The exception height sheep count is always odd.

Given a group of N numbers, representing heights of sheep in kilkili, you are asked to find the unique height that repeated odd times.

Input Format

First line contains an integer T, representing the number of testcases to follow.

The first line of each testcase contains an integer N, denoting the number of sheeps in kilkili species.

Next line consists of N heights with space sepration.

Constraints

1 <= T <= 20

1 <= N <= 10^5

Output Format

For i'th testcase, Print on a new line "Case %d: x", where x denotes the answer to the i'th testcase.

Sample Input 0

2
5
1 2 1 2 3
11
4 4 5 5 4 4 2 2 7 7 7
Sample Output 0

Case 1: 3
Case 2: 7
Submissions: 25
Max Score: 100
Difficulty: Medium
Rate This Challenge:

    
More
 
'''
T=int(input())
for f in range(T):
    K=int(input())
    s=list(map(int,input().split()))
    l={}
    for i in s:
        if i in l:
            l[i]+=1 
        else:
            l[i]=1 
    for i in l:
        if l[i]%2!=0:
            print("Case {}: {}".format(f+1, i))
            break