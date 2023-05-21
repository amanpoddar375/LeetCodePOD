class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_i, start_j = next((i, j) for i in range(m)
                                for j in range(n) if grid[i][j])

        stack = [(start_i, start_j)]
        visited = set(stack)
        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in visited:
                    stack.append((x, y))
                    visited.add((x, y))

        ans = 0
        queue = list(visited)
        while queue:
            new_queue = []
            for i, j in queue:
                for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                        if grid[x][y] == 1:
                            return ans
                        new_queue.append((x, y))
                        visited.add((x, y))
            queue = new_queue
            ans += 1

# TC : O(m * n), where m is the number of rows and n is the number of columns in the grid.
    # Building the initial island using DFS: O(m * n), as each cell is visited at most once.
    # Finding the shortest bridge using BFS: O(m * n), as each cell is visited at most once.
# SC : O(m * n).
