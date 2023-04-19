class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      total_sum = nums[0]
      curr_sum = nums[0]
      for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            total_sum = max(total_sum, curr_sum)
      return total_sum