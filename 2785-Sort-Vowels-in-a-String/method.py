class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)
        return ''.join([vowels.pop() if c.lower() in 'aeiou' else c for c in s])
