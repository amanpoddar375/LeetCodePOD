class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        tower = [[0.0] * 101 for _ in range(101)]
        tower[0][0] = poured
        
        for i in range(query_row + 1):
            for j in range(i + 1):
                overflow = (tower[i][j] - 1.0) / 2.0
                if overflow > 0:
                    tower[i + 1][j] += overflow
                    tower[i + 1][j + 1] += overflow
        
        return min(1.0, tower[query_row][query_glass])

# TC : O(query_row^2)
# SC : O(query_row^2)
