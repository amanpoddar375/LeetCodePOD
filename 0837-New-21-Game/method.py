class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        curr = 1.0
        ans = 0.0

        dp[0] = 1.0

        for i in range(1, n + 1):
            dp[i] = curr / maxPts

            if i < k:
                curr+= dp[i]
            else:
                ans += dp[i]

            if i - maxPts >= 0:
                curr -= dp[i - maxPts]

        return ans

# TC : O(n), where n is the input parameter representing the target number of point
# SC : O(n)