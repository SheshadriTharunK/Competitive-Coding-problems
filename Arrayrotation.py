n,d=map(int,input().split())
arr=list(map(int,input().split()))
arr1=[]
i=0
while(i<d):
    arr1.append(arr[i])
    i+=1
arr2=arr[d:]
arr=arr2+arr1 
print(*arr)