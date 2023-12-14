class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        diff = [[0] * n for _ in range(m)]
        onesRow = [sum(row) for row in grid]
        zerosRow = [n - ones for ones in onesRow]
        onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        zerosCol = [m - ones for ones in onesCol]
        for i in range(m):
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

        return diff