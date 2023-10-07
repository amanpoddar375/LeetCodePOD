class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        if m < k:
            return 0
        dp = [[1] * m] + [[0] * m for _ in range(k - 1)]
        mod = 10 ** 9 + 7
        
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                cur = 0
                for j in range(m):
                    dp[i][j] = (dp[i][j] * (j + 1) + cur) % mod
                    if i:
                        cur = (cur + dp[i - 1][j]) % mod
        
        return sum(dp[-1]) % mod
    
# TC :  O(n * m * k), 
# where n is the input parameter n.
# m is the input parameter m.
# k is the input parameter k.

# SC :  O(k * m),where
# k is the input parameter k.
# m is the input parameter m.