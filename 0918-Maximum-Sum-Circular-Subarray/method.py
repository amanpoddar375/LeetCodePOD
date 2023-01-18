class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = curr_max = min_sum = curr_min = nums[0]
        total_sum = nums[0]
        for i in range(1, len(nums)): 
            total_sum += nums[i]
            curr_max = max(nums[i], curr_max + nums[i]) 
            max_sum = max(max_sum, curr_max)
            curr_min = min(nums[i], curr_min + nums[i]) 
            min_sum = min(min_sum, curr_min)    
        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum
      
# TC : O(n)
# SC : O(1)
