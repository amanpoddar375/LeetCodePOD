class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        for char in set(s):
            first, last = s.find(char), s.rfind(char)
            if first != last:
                count += len(set(s[first+1:last]))
        return count
