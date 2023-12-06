class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        curr = 1
        for i in range(1, n+1):
            total += curr
            curr += 1
            if i % 7 == 0:
                curr = i//7 + 1
        return total

# TC : O(n), where n is the input parameter representing the number of days.
# SC : O(1)