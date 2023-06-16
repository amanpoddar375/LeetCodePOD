class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def count_permutations(arr):
            if len(arr) <= 2:
                return 1

            left = [num for num in arr if num < arr[0]]
            right = [num for num in arr if num > arr[0]]

            return comb(len(left) + len(right), len(right)) * count_permutations(left) * count_permutations(right)

        return (count_permutations(nums) - 1) % (10 ** 9 + 7)

# TC : O(2^n)
# SC : O(n)