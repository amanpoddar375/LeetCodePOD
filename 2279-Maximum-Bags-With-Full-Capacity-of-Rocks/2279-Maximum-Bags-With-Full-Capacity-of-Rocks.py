class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        fullBags = [capacity[i] - rocks[i] for i in range(n)]
        fullBags.sort()
        count = 0
        for x in fullBags:
            if additionalRocks >= x:
                additionalRocks -= x
                count += 1
        return count
