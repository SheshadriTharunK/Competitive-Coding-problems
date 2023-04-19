def leaders(A, N):
        l=[]
        for i in range(len(A)):
          if all((A[i]>A[j]) for j in range(i+1,N)):
             l.append(A[i])
        return l
N=int(input())
A=list(map(int,input().split()))
print(leaders(A, N))





'''n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2

Input:
n = 5
A[] = {1,2,3,4,0}
Output: 4 0


'''