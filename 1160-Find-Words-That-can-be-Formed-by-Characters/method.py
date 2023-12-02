class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def is_good_string(word, char_count):
            for char in word:
                if word.count(char) > char_count.get(char, 0):
                    return False
            return True
        
        char_count = {}
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1

        total_length = 0
        for word in words:
            if is_good_string(word, char_count.copy()):
                total_length += len(word)

        return total_length
