
class Solution:
    def trailingZeroes(self, N):
        fact=1 
        for i in range(1,N+1):
            fact=fact*i 
        count=0
        k=str(fact)
        for i in range(len(k)-1,-1,-1):
            if k[i]=='0':
                count+=1 
            else:
                break 
        return count