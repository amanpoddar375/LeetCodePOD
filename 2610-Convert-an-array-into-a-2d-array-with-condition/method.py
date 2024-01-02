from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        return [[key] * count_map.pop(key) for key in sorted(count_map, reverse=True)]
