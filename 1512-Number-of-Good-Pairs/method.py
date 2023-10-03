class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    result += 1
        return result

# TC : O(n^2)
# SC : O(1)