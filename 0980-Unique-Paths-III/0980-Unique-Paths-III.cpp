class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        int startRow, startCol, endRow, endCol;
        int emptySquares = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == 1) {
                    startRow = i;
                    startCol = j;
                } else if (grid[i][j] == 2) {
                    endRow = i;
                    endCol = j;
                } else if (grid[i][j] == 0) {
                    emptySquares++;
                }
            }
        }
        return dfs(grid, startRow, startCol, endRow, endCol, emptySquares);
    }
private:
    int dfs(vector<vector<int>>& grid, int row, int col, int endRow, int endCol, int emptySquares) {
        if (row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size() || grid[row][col] == -1) {
            return 0;
        }
        if (grid[row][col] == 2) {
            return emptySquares == -1 ? 1 : 0;
            }
        grid[row][col] = -1;
        emptySquares--;
        int paths =dfs(grid, row + 1, col, endRow, endCol, emptySquares)\
        + dfs(grid, row - 1, col, endRow, endCol, emptySquares)\
        + dfs(grid, row, col + 1, endRow, endCol, emptySquares)\
        + dfs(grid, row, col - 1, endRow, endCol, emptySquares);
        grid[row][col] = 0;
        emptySquares++;
        return paths;
    }
};
