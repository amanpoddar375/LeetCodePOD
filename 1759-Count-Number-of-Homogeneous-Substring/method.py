class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        result = 0
        count = 0

        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                count += 1
            else:
                count = 1

            result = (result + count) % MOD

        return result

# TC : O(n)
# SC : O(1)