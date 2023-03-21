class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, left, right = 0, 0, 0    
        while right < len(nums):
            if nums[right] == 0:
                count += right - left + 1
                right += 1
            else:
                left = right + 1
                right = left
        return count

# TC : O(n), where n is the length of the input array. This is because we iterate through the array exactly once, and perform a constant amount of work for each element.

# SC : O(1). We use a constant amount of extra space to store the count, left, and right variables, and we don't create any new data structures.
