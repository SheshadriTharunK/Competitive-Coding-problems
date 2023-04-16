a,b,c,d,e=3,5,4,1,2
k=a,b,c,d,e 
alist=list(k)
for i in range(len(alist)):
    for j in range(0,len(alist)-i-1):
        if alist[j]>alist[j+1]:
            alist[j],alist[j+1]=alist[j+1],alist[j]
           
    for i in range(len(alist)):
        print(alist[i],end=' ')
    print('')