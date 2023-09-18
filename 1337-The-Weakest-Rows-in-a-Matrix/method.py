class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength_rows = [(sum(row), i) for i, row in enumerate(mat)]
        strength_rows.sort()
        result = [row[1] for row in strength_rows[:k]]
        return result

# TC : O(m * log(m)), where m is the number of row in the matrix
# SC : O(m)