class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += rows - row  # Increment count by the remaining elements in the column
                col -= 1
            else:
                row += 1

        return count

# TC : O(m+n), where 'm' is the number of rows in the grid and 'n' is the number of columns in the grid. Since we start from the top-right corner and move left or down, we traverse at most 'm + n' elements.

# SC : O(1), as the space usuage does not depend on the size of input