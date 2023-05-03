n=int(input())
if n==1:
    print('+')
if n==2:
    print('+')
    print('+',end='')
    print('-',end='')
    print('+')
if n>2:
    k=1
    print('+')
    for i in range(1,n-1):
        print('|',end='')
        print(' '*(2*k-1),end='')
        print('\\')
        k+=1
    print('+',end='')
    print('-'*(2*k-1),end='')
    print('+')
    