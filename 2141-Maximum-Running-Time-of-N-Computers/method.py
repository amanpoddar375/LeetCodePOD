class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        s = sum(batteries)
        while batteries[-1] > (s / n):
            n -= 1
            s -= batteries.pop()
        return int(s / n)
    

# TC : O(n log n) time complexity, where n is the number of computers.
# SC : O(n)