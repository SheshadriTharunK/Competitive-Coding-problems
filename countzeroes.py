'''CountZeroes
Problem
Submissions
Leaderboard
Discussions
Given a sequence that consists of zeroes followed by non-zero integers, your task is to count the number of zeroes.

Input Format

First line consists of size of the sequence, N.

Second line consists of N integers of the sequence.

Constraints

1 <= N <= 10^9

Output Format

A single line consisting of count of zeroes.

Sample Input 0

10
0 0 0 0 0 0 10 9 8 7
Sample Output 0

6

'''
from bisect import bisect_left,bisect_right
T=int(input())
l=list(map(int,input().split()))
print(bisect_right(l,0)-bisect_left(l,0))
