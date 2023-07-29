class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
            
        memo = {}
        
        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            memo[(a, b)] = 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) + dfs(a - 25, b - 75))
            return memo[(a, b)]
        return dfs(n, n)
