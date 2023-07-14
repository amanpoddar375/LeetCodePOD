class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        longest_length = 0

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1

            longest_length = max(longest_length, dp[num])

        return longest_length


# TC : O(n), where n is the length of the input array arr.
# SC : O(n), where n is the length of the input array arr.