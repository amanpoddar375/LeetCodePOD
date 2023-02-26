class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j   
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[m][n]
      
''' TC : O(mn), where m and n are the lengths of the input strings word1 and word2 respectively. 
This is because we are filling up a 2D table of size (m+1)x(n+1) using nested loops. '''

''' SC: O(mn), same as the time complexity, as we are using a 2D table of size (m+1)x(n+1) to store the minimum edit distances.'''
