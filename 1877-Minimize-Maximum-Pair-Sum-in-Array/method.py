class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        max_pair_sum = float('-inf')

        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - i - 1]
            max_pair_sum = max(max_pair_sum, pair_sum)

        return max_pair_sum
    
# TC : O(n log n), where n is the length of the input array nums. 
# SC : O(1)