class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                result.append(self.justify_line(line, maxWidth, False))
                line = [word]
                line_length = len(word)
        
        result.append(self.justify_line(line, maxWidth, True))
        return result
    
    def justify_line(self, line, maxWidth, is_last_line):
        if is_last_line or len(line) == 1:
            return ' '.join(line).ljust(maxWidth)
        
        total_spaces = maxWidth - sum(len(word) for word in line)
        spaces_between_words = total_spaces // (len(line) - 1)
        extra_spaces = total_spaces % (len(line) - 1)
        
        justified_line = line[0]
        for i in range(1, len(line)):
            spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
            justified_line += ' ' * spaces + line[i]
        
        return justified_line

# TC : O(n)
# SC : O(n)