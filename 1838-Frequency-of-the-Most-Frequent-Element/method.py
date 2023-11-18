class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_freq = 0
        left = 0
        total_ops = 0

        for right in range(n):
            total_ops += nums[right]

            while (right - left + 1) * nums[right] - total_ops > k:
                total_ops -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq