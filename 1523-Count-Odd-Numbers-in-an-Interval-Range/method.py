class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            count += 1
        return count
#TC : O(1)
