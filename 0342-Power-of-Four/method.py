class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        digit = math.log(n, 4)
        return digit.is_integer()
    
# TC : O(1)
# SC : O(1)