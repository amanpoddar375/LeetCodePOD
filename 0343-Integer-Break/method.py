class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)

        dp[2] = 1
        dp[3] = 2
        
        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], j * max(i - j, dp[i - j]))
        
        return dp[n]

# TC : O(n^2)
# SC : O(n)