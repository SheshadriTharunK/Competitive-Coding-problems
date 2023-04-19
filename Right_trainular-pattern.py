n=int(input())
if n==1:
    print('+')
if n==2:
    print("+")
    print("+",end='')
    for i in range(1,n):
        print("-",end='')
    print("+")
if n>2:
    print("+")
    for i in range(1,n):
        if i==n-1:
                    print("+", end="")
                    print('-'*(2*i-1),end='')
                    print("+")
        else:
                print("|",end='')
                print(' '*(2*i-1),end='\\')
                print()