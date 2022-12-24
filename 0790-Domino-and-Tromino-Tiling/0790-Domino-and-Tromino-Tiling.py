class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        
        mod = 10 ** 9 + 7
        dp = [0] * n
        dp_incomp = [0] * n
        
        dp[0] = 1
        dp[1] = 2
        dp_incomp[1] = 2
        
        for i in range(2, n):
            dp[i] = (dp[i - 2] + dp[i - 1] + dp_incomp[i - 1]) % mod
            dp_incomp[i] = (dp[i - 2] * 2 + dp_incomp[i - 1]) % mod
        
        return dp[n-1] % mod
