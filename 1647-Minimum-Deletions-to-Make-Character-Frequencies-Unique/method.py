class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0) + 1

        seen_freqs = set()
        deletions = 0
        
        for char, char_freqs in freq.items():
            while char_freqs in seen_freqs:
                char_freqs -= 1
                deletions += 1
            if char_freqs > 0:
                seen_freqs.add(char_freqs)
        
        return deletions

# TC : O(n), where n is the length of the input string s
# SC : O(k), where k is the number of unique character frequencies in the string