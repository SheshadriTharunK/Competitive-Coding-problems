
class Solution:
  
    def maxSubArraySum(self,arr,N):
         arr_count=arr[0]
         max_count=arr[0]
         for i in range(1,len(arr)):
             arr_count=max(arr_count+arr[i],arr[i])
             max_count=max(arr_count,max_count)
         return max_count

