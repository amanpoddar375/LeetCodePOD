class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def findRightmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        leftmost = findLeftmost(nums, target)
        rightmost = findRightmost(nums, target)
        
        if leftmost <= rightmost:
            return [leftmost, rightmost]
        else:
            return [-1, -1]

# TC : O(log n), where n is the length of the input array.
# SC : O(1)