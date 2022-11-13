class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.strip()
        string_list = r.split()
        string_list.reverse()
        return (' '.join(string_list))