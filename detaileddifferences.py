a=int(input())
for i in range(a):
    x1=input()
    x2=input()
    print(x1)
    print(x2)
    for i in range(len(x1)):
        if x1[i]==x2[i]:
              print('.',end='')
        else:
                print('*',end='')
    print("\n")