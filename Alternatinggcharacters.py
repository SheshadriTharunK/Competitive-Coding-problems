'''You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

Example:
S=AABAAB
Remove an A positions 0 and 3 to make s=ABAB in deletions

Remove an  at positions  and  to make  in  deletions.

Function Description:


Complete the alternatingCharacters function in the editor below.

alternatingCharacters has the following parameter(s):

string s: a string
Returns

int: the minimum number of deletions required
Input Format

The first line contains an integer , the number of queries.
The next  lines each contain a string  to analyze.

Constraints:
*1<=q<=10
*1<=length of s<=10^5 


Each string  s  will consist only of characters A  and B .
Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Sample Output

3
4
0
0
4
Explanation

The characters marked red are the ones that can be deleted so that the string does not have matching adjacent characters.'''















T=int(input())
for i in range(T):
    s=input()
    count=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
    print(count)
