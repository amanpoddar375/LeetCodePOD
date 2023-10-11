class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))
        n = len(nums)
        result = n
        for i, left in enumerate(unique_nums):
            right = left + n -1
            pos = bisect_right(unique_nums,right)
            uniqueLen = pos - i
            result = min(result, n - uniqueLen)
        return result

# TC : O(nlogn)
# SC : O(n)