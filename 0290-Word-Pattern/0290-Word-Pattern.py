class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if(len(words)) != len(pattern):
            return False
        mapping = {}
        for i in range (len(pattern)):
            char = pattern[i]
            word = words[i]
            if char not in mapping:
                if word in mapping.values():
                    return False
                mapping[char] = word
            elif mapping[char] != word:
                return False
        return True

''' TC: O(n), where n is the number of characters in the pattern. 
This is because the function loops through the characters in the pattern once, 
and each operation inside the loop takes constant time.'''

''' SC: O(n), because the function stores the mappings between characters and words in a hash map, 
which has a size of at most n, and the function also stores the visited words in a set, 
which also has a size of at most n. '''
