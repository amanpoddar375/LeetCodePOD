class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        operations = 0
        current_max = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] < current_max:
                current_max = nums[i]
                operations += n - 1 - i

        return operations