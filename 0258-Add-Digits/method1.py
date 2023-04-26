class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(list(map(int, str(num))))
        return num
# TC: O(N log N), where N is the value of num.
# SC: O(log N), where N is the value of num.
