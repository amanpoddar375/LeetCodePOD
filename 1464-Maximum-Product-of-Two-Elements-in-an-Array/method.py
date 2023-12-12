class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i):
                ans = (nums[i]-1) * (nums[j] -1)
                result.append(ans)

        return max(result)
    
# TC : O(n^2), where n is the length of the nums
# SC : O(n^2)