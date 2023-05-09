class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        left, right, up, down = 0, cols - 1, 0, rows - 1

        while len(ans) < rows * cols:
            #from left to right
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            #from up to down
            for j in range(up, down+1):
                ans.append(matrix[j][right])
            right -= 1
            #from right to left
            if up <= down:
                for k in range(right, left-1, -1 ):
                    ans.append(matrix[down][k])
                down -= 1

            #from bottom to top
            if left <= right:
                for l in range(down, up-1, -1):
                    ans.append(matrix[l][left])
                left += 1
            
        return ans

# TC : O(m * n), where m is the number of rows and n is the number of columns in the input matrix

# SC : O(m * n), which is the size of the output list containing the spiral order of the input matrix.
