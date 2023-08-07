class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1

        while row < rows and col > -1:
            cur = matrix[row][col]
            if cur == target:
                return True
            elif target > cur:
                row += 1
            else:
                col -= 1
        
        return False

# TC : O(m + n), where m is the number of rows in the matrix and n is the number of columns.
# SC : O(1)