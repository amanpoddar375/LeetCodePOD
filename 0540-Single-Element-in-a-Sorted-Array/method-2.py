# Binary Search
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return nums[left]
      
# TC : O(logn), This is because the algorithm performs a binary search on the array, halving the search range at each iteration.
# SC : O(1),only uses a few variables to keep track of the search range and the middle index, so the space usage is constant and independent of the size of the input array.
