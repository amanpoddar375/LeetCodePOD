class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create a table to store results of subproblems
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        # Fill dp[][] in bottom up manner 
        for i in range(m+1):
            for j in range(n+1):
                # If first string is empty, only option is to 
                # insert all characters of second string 
                if i == 0:
                    dp[i][j] = j  # Min. operations = j 

                # If second string is empty, only option is to 
                # remove all characters of second string 
                elif j == 0:
                    dp[i][j] = i  # Min. operations = i 

                # If last characters are same, ignore last char 
                # and recur for remaining string 
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                # If the last character is different, consider all 
                # possibilities and find the minimum 
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],  # Insert 
                                       dp[i-1][j],  # Remove 
                                       dp[i-1][j-1])  # Replace 

        return dp[m][n]
