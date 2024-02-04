'''StringQuery
You are given two strings: an input string S, and a command string C. The command string is composed of two different commands:

P, or pop, removes the first letter from the input string and returns the letter
R, or reverse, reverses the input string
Given S and C, your task is to compute the output string after applying all the commands of C on S. The input string is not guaranteed to be empty even after all the commands are executed. So, return whatever is in the output string after finishing commands.

Input Format

The first line contains an input string S.
The second line contains a command string C.
Constraints

1 <= len(S) <= 10^6
1 <= len(C) <= 10^6
S contains only alphanumeric characters
C contains only two letters: P and R
There will never be a pop from an empty input string
Output Format

Output a line consisting of the output string.

Sample Input 0

Agrtmcaihiol
PRPRPRPRPRPRPRPRPRPRPRPR
Sample Output 0

Algorithmica
Sample Input 1

Thingnik
PPPPRPPPP
Sample Output 1

Thinking'''
from collections import deque 
s=deque(list(input()))
c=input()
l=[]
o=''
count=0 
for i in c:
    if  i=='R':
         r=True 
         count+=1 
    elif i=='P' and count%2==0:
        l.append(s.popleft())
    else:
        l.append(s.pop())
s=''.join(map(str,l))
print(s)
