class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
''' TC : O(m*n), where m is the length of the haystack and n is the length of the needle.
In the worst case scenario, the function would need to compare every character of the haystack with the needle. '''

''' SC : O(1), as no additional space is used except for a few constant variables. '''
