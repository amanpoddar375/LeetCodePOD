class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        n1 = len(a)
        n2 = int((len(a) + 1)/2)
        if n1 % 2 == 0:
            return (a[n2-1] + a[n2])/2
        else:
            return a[n2-1]

# TC : O((n1 + n2) * log(n1 + n2)), where n1 and n2 are the lengths of nums1 and nums2, respectively.
# SC : O(n1 + n2)