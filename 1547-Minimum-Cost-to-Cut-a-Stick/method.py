class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[float('inf')] * m for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):
                if j - i == 1:
                    dp[i][j] = 0
                else:
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
        
        return dp[0][m - 1]

# TC : O(n^3), where n is the length of the cuts list.
# SC : O(n^2)