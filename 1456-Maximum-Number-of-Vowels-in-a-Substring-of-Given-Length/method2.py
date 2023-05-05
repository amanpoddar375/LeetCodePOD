class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowels = 0
        curr_vowels = 0

        # Loop through the string s using a sliding window of length k
        for i in range(len(s) - k + 1):
            # Count the number of vowels in the current window of length k
            for j in range(i, i + k):
                if s[j] in vowels:
                    curr_vowels += 1

            # Update the maximum number of vowels seen so far        
            max_vowels = max(curr_vowels, max_vowels)

            # Reset the current number of vowels for the next window
            curr_vowels = 0
            
        return max_vowels

# TC : O(nk)
# SC : O(1)
