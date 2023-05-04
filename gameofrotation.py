n=int(input())
arr=list(map(int,input().split()))
l=[]
for k in range(len(arr)):
    
    sum=0
    i=1
    while(i<2):
        a1=arr[1:]
        a2=arr[:1]
        arr=a1+a2
        i=i+1
    for i in range(len(arr)):
        sum+=(i+1)*arr[i]
        a=sum  
    l.append(a)
print(max(l))sameof