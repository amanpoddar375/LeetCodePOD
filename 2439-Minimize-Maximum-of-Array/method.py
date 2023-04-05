class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s, res = 0, 0
        for i in range(len(nums)):
            s += nums[i]
            res = max(res, (s + i) // (i + 1))
        return res
# TC : O(nlog(max(nums)) where n is the length of nums and max(nums) is the maximum element in nums. 
# SC : O(1). The algorithm only uses a constant amount of extra space.
