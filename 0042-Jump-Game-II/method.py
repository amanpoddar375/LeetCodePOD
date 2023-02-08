class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        lastpos = 0
        end = 0
        for i in range(len(nums) - 1):
            lastpos = max(lastpos, i + nums[i])
            if lastpos >= len(nums) - 1:
                jumps += 1
                break
            if i == end:
                jumps += 1
                end = lastpos
        return jumps
