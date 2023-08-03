class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_letters = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        combinations = ['']
        for digit in digits:
            new_combinations = []
            for letter in digit_letters[digit]:
                for combination in combinations:
                    new_combinations.append(combination + letter)
            combinations = new_combinations

        return combinations

# TC : O(4^n)
# SC : O(4^n)