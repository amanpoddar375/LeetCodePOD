class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [0] * n
        prefix_sum = [0] * (n + 1)

        # Calculate prefix sum
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Calculate averages using prefix sum
        for i in range(n):
            left = max(i - k, 0)
            right = min(i + k, n - 1)
            count = right - left + 1

            if count < 2 * k + 1:
                avgs[i] = -1
            else:
                subarray_sum = prefix_sum[right + 1] - prefix_sum[left]
                avgs[i] = subarray_sum // count

        return avgs

# TC : O(n)
# SC : O(n)