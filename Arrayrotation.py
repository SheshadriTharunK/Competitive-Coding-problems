'''Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

Examples:  

Input: 
arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3 4 5 6 7 1 2

Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
Output: 5 6 7 1 2 3 4'''
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
