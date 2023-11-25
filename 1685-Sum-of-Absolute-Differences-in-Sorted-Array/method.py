class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        result = [0] * n

        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        for i in range(n):
            left_sum = i * nums[i] - prefix_sum[i]
            right_sum = suffix_sum[i] - (n - i - 1) * nums[i]
            result[i] = left_sum + right_sum

        return result