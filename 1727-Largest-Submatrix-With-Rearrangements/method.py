class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
        for row in matrix:
            row.sort(reverse=True)
        max_area = 0
        for i in range(m):
            for j in range(n):
                max_area = max(max_area, matrix[i][j] * (j + 1))
        return max_area