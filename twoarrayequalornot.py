#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        A.sort()
        B.sort()
        if all(A[i]==B[i] for i in range(len(A))):
            return 1 
        else:
            return 0
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
                
                
# } Driver Code Ends