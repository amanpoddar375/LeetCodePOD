class Solution:
    def countDigits(self, num: int) -> int:
        digit = list(str(num))
        count = 0
        for i in range (len(digit)):
            if num % int(digit[i]) == 0:
                count= count + 1
        return count
