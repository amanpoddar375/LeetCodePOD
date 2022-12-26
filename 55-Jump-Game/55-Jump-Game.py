class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastpos = 0
        for i in range(len(nums)):
            if i > lastpos: return False
            lastpos = max(lastpos, i + nums[i])
        return True

#TC : O(n) because the loop iterates through the array once, and the rest of the operations inside the loop are constant time operations.
#SC : O(1) because the only additional space used is a single integer variable to keep track of the last position that can be reached.
