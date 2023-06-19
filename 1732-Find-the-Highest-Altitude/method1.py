class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        levels = [0]
        for i in range(len(gain)):
            levels.append(levels[i] + gain[i])
        return max(levels)

# TC : O(n)
# SC : O(n)