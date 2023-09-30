class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        reverse_num = nums[::-1]
        collected = set()
        target_set = set(range(1, k + 1))

        for num in reverse_num:
            collected.add(num)
            ops+=1

            if target_set.issubset(collected):
                break

        return ops

# TC : O(n), where n is the length of input nums
# SC : O(k)