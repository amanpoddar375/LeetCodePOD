class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        pigs = 0
        while (states ** pigs) < buckets:
            pigs += 1
        return pigs

# TC : O(log(n)), where "n" is the number of buckets. 
# SC : O(1)