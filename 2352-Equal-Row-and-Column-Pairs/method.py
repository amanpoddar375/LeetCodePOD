class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(zip(*grid)):
                if row == list(col):
                    count += 1
        return count

# TC : O(n^2)
# SC : O(n)