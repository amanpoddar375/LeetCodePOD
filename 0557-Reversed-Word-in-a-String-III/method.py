class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)


# TC : O(n), where n is the total number of character in input string s
# SC : O(n)