'''Given an integer n, write a function that returns count of trailing zeroes in n!. 
Examples : 

Input: n = 5
Output: 1 
Factorial of 5 is 120 which has one trailing 0.

Input: n = 20
Output: 4
Factorial of 20 is 2432902008176640000 which has
4 trailing zeroes.

Input: n = 100
Output: 24'''










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
