class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split()
        string_list.reverse()
        return (' '.join(string_list))