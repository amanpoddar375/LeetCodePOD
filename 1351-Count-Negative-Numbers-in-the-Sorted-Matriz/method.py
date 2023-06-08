class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count+=1
        return count

# TC : O(m*n), where 'm' is the number of rows in the grid and 'n' is the number of columns in the grid.

# SC : O(1), as the space usuage does not depend on the size of input