class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if k < 10:
            return len(s) if k >= int(max(s)) else -1
        digits = len(str(k))
        count = 0
        while s:
            if s[:digits] <= str(k):
                s = s[digits:]
            else:
                s = s[digits-1:]
            count += 1
        return count
#TC : O(n), where n is the length of the string s, because it iterates through the digits of s once
#SC : O(1), as it only uses a constant amount of memory.
