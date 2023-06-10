'''
Special Transformer
You are given two strings: an input string, and an operations string. You must use the following operations to turn the input string into a new output string.

The operations string is composed of two different commands:

P, or pop, removes the first letter from the input string and places it at the end of the output string.
R, or reverse, reverses the input string.
There will never be a pop from an empty input string. The output string starts off empty.

Output the new string produced by these commands. The input string is not guaranteed to be empty even after all the commands are executed; return whatever is in the output string at the time.

Input Format

The first line will contain input string I. I will only contain alphanumeric characters.

The second line will contain operations string C. C will only contain two letters: P and R.

Constraints

1 <= len(I) <= 10^6

1 <= len(C) <= 10^6

Output Format

Output a single string O, the output string.

Sample Input 0

1soloCIPC
RPPRPRPRPRPPRPP
Sample Output 0

CP1IsCool
'''
from collections import deque 
ip=input()
op=input()
output=[]
ip=deque(ip)
rev=False 
for i in op:
    if i=='R':
        rev=not rev 
    elif i=='P' and rev==True:
        a=ip.pop()
        output.append(a)
    elif i=='P' and rev==False:
        a=ip.popleft()
        output.append(a)
o=''.join(output)
print(o)