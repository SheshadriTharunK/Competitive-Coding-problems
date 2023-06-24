'''TotCount

There are n children standing in a line and a child X is called Tot if all the children standing to the left of her are having height < height(X) and all the children standing to the right of her are haveing height > height(X).

Given the heights of N children, your task is to find all the Tots.

Input Format

A single line consisting of N, the number of children.

Next line consists of heights of N children.

Constraints

3 <= N <= 10^6

Output Format

A single line with count of Tots.

Sample Input 0

8
2 1 3 4 7 5 6 8
Sample Output 0

3
Sample Input 1

3
1 2 3
Sample Output 1

3'''
n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
count=0
for i in range(len(a)):
    if a[i]==b[i]:
        count+=1 
print(count)