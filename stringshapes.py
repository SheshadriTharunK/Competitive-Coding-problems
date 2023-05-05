s,a=map(str,input().split(' '))
if a=='Rectangle':
    print(s+s[0])
    for i in range(1,len(s)):
        print(s[len(s)-i],end='')
        print(' '*(len(s)-1),end='')
        print(s[i])
    print(s[0]+s[::-1])
elif a=='Triangle':
    k=2
    for i in range(len(s)):
        if i==0:
            print(' '*(len(s)-1),end='')
            print(s[-1]+s[-1])
        else:
            print(' '*(len(s)-i-1),end='')
            print(s[len(s)-i-1],end='')
            print(' '*k,end='')
            print(s[len(s)-i-1])
            k+=2
    print(s+s[::-1])