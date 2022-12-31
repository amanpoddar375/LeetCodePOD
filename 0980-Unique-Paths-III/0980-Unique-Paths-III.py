class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_row, start_col, end_row, end_col = 0, 0, 0, 0
        empty_squares = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    start_row = i
                    start_col = j
                elif grid[i][j] == 2:
                    end_row = i
                    end_col = j
                elif grid[i][j] == 0:
                    empty_squares += 1
        return self.dfs(grid, start_row, start_col, end_row, end_col, empty_squares)
    
    def dfs(self, grid: List[List[int]], row: int, col: int, end_row: int, end_col: int, empty_squares: int) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == -1:
            return 0
        if grid[row][col] == 2:
            return 1 if empty_squares == -1 else 0
        grid[row][col] = -1
        empty_squares -= 1
        paths = self.dfs(grid, row + 1, col, end_row, end_col, empty_squares) \
            + self.dfs(grid, row - 1, col, end_row, end_col, empty_squares) \
            + self.dfs(grid, row, col + 1, end_row, end_col, empty_squares) \
            + self.dfs(grid, row, col - 1, end_row, end_col, empty_squares)
        grid[row][col] = 0
        empty_squares += 1
        return paths
