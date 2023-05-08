class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_sum= sum(mat[i][i] for i in range(n))
        secondary_sum = sum(mat[i][n-i-1] for i in range(n))
        if n % 2 == 1:
            center = mat[n//2][n//2]
            return primary_sum + secondary_sum -center 
        else:
            return primary_sum + secondary_sum

# TC : O(n).

# SC : O(1), Only constant extra space is used for storing variables.
