class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        num = 1
        rowstart, rowend = 0, n-1
        colstart, colend = 0, n-1

        while rowstart <= rowend and colstart<=colend:
            #from left to right
            for i in range(colstart, colend + 1):
                matrix[rowstart][i] = num
                num += 1
            rowstart += 1

            #from top to bottom
            for j in range(rowstart, rowend + 1):
                matrix[j][colend] = num
                num+=1
            colend -= 1

            #from right to left
            if rowstart <= rowend:
                for i in range(colend,colstart -1, -1):
                    matrix[rowend][i] = num
                    num+=1
                rowend -= 1
                
            #from bottom to top
            if colstart <= colend:
                for j in range(rowend, rowstart -1, -1):
                    matrix[j][colstart] = num
                    num+=1
                colstart += 1
        return matrix
            
# TC : O(n^2), as it must iterate over every element in the matrix exactly once.
# SC : O(n^2), as it creates a new 2D array with n rows and n columns to hold the output matrix.
