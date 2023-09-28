class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x%2 == 0]
        odd = [x for x in nums if x%2 != 0]
        return even + odd

# TC : O(n), where n is the length of input nums array
# SC : O(n), where n is the length of input nums array