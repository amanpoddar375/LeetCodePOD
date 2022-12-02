class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1 = Counter(Counter(word1).values())
        s2 = Counter(Counter(word2).values())
        return s1 == s2  and set(word1) == set(word2)