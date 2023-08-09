class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = 0
            j = 1
            while j < n:
                if nums[j] - nums[j-1] <= mid :
                    count += 1
                    j += 1
                j += 1
            if count >= p:
                right = mid
            else:
                left = mid + 1
        return left

# TC : O(nlogn), where n is the length of the nums
# SC : O(1)