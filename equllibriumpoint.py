'''
A sequence of poles are built as part of constructing a suspension bridge. A Balancing pole, p, in a sequence is defined as a pole where the weight will be balanced i.e., sum of the weights of all the left poles from p is equal to the sum of the weights of all the right poles from p.

You have given a sequence of integers representing the pole weights, write a program that returns the index of the balancing pole. If no such index exists, then return -1. If there are multiple balancing poles, then return the index of left most balancing pole.

Input Format

A single line consisting of N, the number of poles.

Next line consists of N weights with space separation.

Constraints

1 <= N <= 10^6

Output Format

A single line with balancing pole index if exists, otherwise -1

Sample Input 0

6
2 6 3 6 4 7
Sample Output 0

3
Sample Input 1

3
2 3 -3
Sample Output 1

0'''
N=int(input())
l=list(map(int,input().split()))
ts=sum(l)
ls=0
for i in range(N):
    if ls==ts-ls-l[i]:
        print(i)
        exit()
    ls+=l[i]
print(-1)



