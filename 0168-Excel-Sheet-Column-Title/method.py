class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber -= 1  # Convert to 0-based index
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result  # Convert to ASCII character ('A' is 65)
            columnNumber //= 26
        
        return result


# TC : O(log(columnNumber, 26))
# SC : O(log(columnNumber, 26))