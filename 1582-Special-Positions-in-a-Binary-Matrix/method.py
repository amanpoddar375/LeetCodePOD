class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        m = len(mat[0])
        n = len(mat)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    # Check if the current position is special
                    if sum(mat[i]) == 1 and sum(mat[k][j] for k in range(n)) == 1:
                        count += 1

        return count