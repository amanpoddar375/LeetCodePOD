class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        dp = [0] + [n + 2] * n
        
        for i in range(n + 1):
            left, right = max(0, i - ranges[i]), min(n, i + ranges[i])
            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[max(0, left)] + 1)
        
        return dp[n] if dp[n] < n + 2 else -1

# TC : O(n^2), where n is the length of the garden
# SC : O(n)