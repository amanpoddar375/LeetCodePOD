class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curralt = 0
        maxalt = 0
        for altgain in gain:
            curralt += altgain
            maxalt = max(curralt, maxalt)
        return maxalt

# TC : O(n)
# SC : O(1)