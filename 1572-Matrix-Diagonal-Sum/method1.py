class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary = []
        secondary = []
        for i in range(n):
            primary.append(mat[i][i])
            secondary.append(mat[i][n-i-1])
        if n % 2 == 1:
            return sum(primary) + sum(secondary) - mat[n//2][n//2]
        else:
            return sum(primary) + sum(secondary)

# TC : O(n^2) where n is the size of the matrix. This is because we need to traverse the entire matrix to compute the diagonal sum.

# SC : O(n) where n is the size of the matrix. This is because we use two arrays to store the primary and secondary diagonal elements.
