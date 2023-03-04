class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        last_invalid_element = -1
        last_minK_idx = -1
        last_maxK_idx = -1
        count = 0
        
        for i in range(n):
            if minK <= nums[i] <= maxK:
                last_minK_idx = i if nums[i] == minK else last_minK_idx
                last_maxK_idx = i if nums[i] == maxK else last_maxK_idx
                count += max(0, min(last_minK_idx, last_maxK_idx) - last_invalid_element)
            else:
                last_invalid_element = i
                last_minK_idx = -1
                last_maxK_idx = -1
                
        return count
# TC : O(n), where n is the length of the input array nums
# SC : O(1), as we are only using constant amount of extra space to store some variables
