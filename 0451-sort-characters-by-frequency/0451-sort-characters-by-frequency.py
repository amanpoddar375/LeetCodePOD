class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(c *ct for c, ct in Counter(s).most_common())
    