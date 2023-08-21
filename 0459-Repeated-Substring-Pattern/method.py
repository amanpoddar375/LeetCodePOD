class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1, n // 2 + 1):
            if n % i == 0:  # If i is a factor of n
                substring = s[:i]
                num_repeats = n // i
                constructed_string = substring * num_repeats
                
                if constructed_string == s:
                    return True
        
        return False

# TC : O(n), where n is the length of the given input string s.
# SC : O(1)