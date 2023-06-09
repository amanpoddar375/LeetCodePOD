class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

# TC : O(n), where n is the length of the letters array.
# SC : O(1) because it uses a constant amount of additional space to store variables (letter).