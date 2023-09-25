#using total cardinal differences
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = 0
        sum_t = 0
        for i in s:
            sum_s += ord(i)
        for j in t:
            sum_t += ord(j)

        diff =  sum_t - sum_s

        return chr(diff)

# TC : O(n), where n is the length of the longer string between s and t
# SC : O(1)