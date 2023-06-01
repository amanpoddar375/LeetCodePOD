from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:  # Check if start or end cell is blocked
            return -1

        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        queue = deque([(0, 0, 1)])  # Queue to store cells for BFS traversal
        grid[0][0] = 1  # Mark the start cell as visited

        while queue:
            x, y, steps = queue.popleft()

            if x == n - 1 and y == n - 1:  # Reached the end cell
                return steps

            for dx, dy in directions:  # Explore 8 neighboring cells
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:  # Valid and unvisited cell
                    queue.append((nx, ny, steps + 1))
                    grid[nx][ny] = 1  # Mark the cell as visited

        return -1  # No clear path found

# TC : O(n^2)
# SC : O(n), because, in the worst case, the BFS queue can contain all the cells in the grid