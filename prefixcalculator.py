'''PrefixCalculator
Problem
Submissions
Leaderboard
Discussions
Implement a program to evaluate a prefix expression consisting of only integers and binary operators (+, -, *, /).

Input Format

The first input will be a single integer N denoting the number of test cases to take.

After this there will be exactly N lines, each line a valid prefix string.

Every integer and operator will be separated by a SPACE. The symbol ‘?’ denotes the end of expression.

Constraints

1 <= N <= 20

1 <= len(expression) <= 10^5

The string will be a valid prefix expression

Output Format

Exactly N lines, each line denoting the output of the expression with two decimal places of precision.

Sample Input 0

1
+ * 30 4 50 ?
Sample Output 0

170.00
'''
T=int(input())
for i in range(T):
    x=input().split()
    x.pop()
    x=x[::-1]
    operands=[]
    for i in x:
        if i.isdigit():
            operands.append(int(i))
        else:
            a=operands.pop()
            b=operands.pop()
            if i=='+':
                operands.append(a+b)
            elif i=='-':
                operands.append(b-a)
            elif i=='*':
                operands.append(a*b)
            elif i=='/':
                operands.append(b/a)
    print("{:0.2f}".format(operands[0]))
