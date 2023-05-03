class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = list(set(nums1) - set(nums2))
        b = list(set(nums2) - set(nums1))
        return [a,b]
# TC : O(n), where n is the length of the input lists.
# Sc : O(n), where n is the length of the input lists.
