class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_arithmetic(subarray: List[int]) -> bool:
            subarray.sort()
            diff = subarray[1] - subarray[0]
            for i in range(1, len(subarray)):
                if subarray[i] - subarray[i - 1] != diff:
                    return False
            return True

        result = []
        for left, right in zip(l, r):
            subarray = nums[left:right + 1]
            result.append(is_arithmetic(subarray))

        return result