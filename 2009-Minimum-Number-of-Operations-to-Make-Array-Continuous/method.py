class Solution:
    def minOperations(self, nums: List[int]) -> int:

        unique_nums = sorted(set(nums))
        n = len(unique_nums)
        maxLen = 0
        left = 0
        
        for right in range(n):
            while unique_nums[right] - unique_nums[left] > n - 1:
                left += 1
            maxLen = max(maxLen, right - left + 1)
        
        return len(nums) - maxLen

# TC : O(nlogn)
# SC : O(n)