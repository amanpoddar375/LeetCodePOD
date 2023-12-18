class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0] * nums[1]
        b = nums[-1] * nums[-2]
        return b-a