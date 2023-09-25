#using XOR
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for i in s:
            c ^= ord(i)
        for j in t:
            c ^= ord(j)
        return chr(c)

# TC : O(n)
# SC : O(1)