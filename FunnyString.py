T=int(input())
for i in range(T):
    s=input()
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for i in range(len(s)):
        l1.append(ord(s[i]))
    sreverse=''.join(reversed(s))
    for i in range(len(s)):
        l2.append(ord(sreverse[i]))
    for i in range(1,len(l1)):
        a=abs(l1[i]-l1[i-1])
        l3.append(a)
    for i in range(1,len(l2)):
        a=abs(l2[i]-l2[i-1])
        l4.append(a)
    if l3==l4:
        print('Funny')
    else:
        print('Not Funny')
