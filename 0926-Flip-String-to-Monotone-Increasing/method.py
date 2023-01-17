class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        countOnes = 0
        countFlips = 0
        for bit in s:
            if bit == '1':
                countOnes += 1
            else:
                countFlips = min(countFlips + 1, countOnes)
        return countFlips
# TC : O(n)
# SC : O(1)
