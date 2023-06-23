class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        longest = 0
        n = len(nums)
        for i in range(n):
            dp[i] = {}

            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                longest = max(longest, dp[i][diff])

        return longest

# TC : O(n^2), where n is the length of the input nums list. 
# SC : O(n^2) as the dp dictionary stores the lengths of arithmetic subsequences for each index and difference pair.