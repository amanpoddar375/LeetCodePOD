class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(arr)) == len(set(Counter(arr).values()))