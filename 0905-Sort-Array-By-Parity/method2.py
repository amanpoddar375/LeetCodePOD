class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x:x%2)
        return nums

# TC : O(n*log(n)), where n is the length of input nums array
# SC : O(1), where n is the length of input nums array