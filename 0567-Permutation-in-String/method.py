class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        char_counts_s1 = [0] * 26
        char_counts_s2 = [0] * 26

        for char in s1:
            char_counts_s1[ord(char) - ord('a')] += 1
        
        for i in range(len(s1)):
            char_counts_s2[ord(s2[i]) - ord('a')] += 1
        
        if char_counts_s1 == char_counts_s2:
            return True

        left = 0
        right = len(s1)
        for i in range(len(s2) - len(s1)):
            char_counts_s2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            char_counts_s2[ord(s2[right-1]) - ord('a')] += 1
            if char_counts_s1 == char_counts_s2:
                return True
        return False
