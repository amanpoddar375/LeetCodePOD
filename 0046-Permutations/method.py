from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)

# TC : O(n!), where n is the length of the input list nums
# SC : O(n!), as it requires generating and storing all the permutations in memory.