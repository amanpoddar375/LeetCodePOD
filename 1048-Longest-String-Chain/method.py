class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_chain = 1
        
        for word in words:
            dp[word] = 1 
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            max_chain = max(max_chain, dp[word])
        
        return max_chain

# TC : O(n*k^2), where n is the number of words, and k is the average length of the words. 
# SC : O(n)