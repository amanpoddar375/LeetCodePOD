class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair_sum = nums1[i] + nums2[j]
                if len(heap) < k:
                    heapq.heappush(heap, (-pair_sum, [nums1[i], nums2[j]]))
                elif pair_sum < -heap[0][0]:
                    heapq.heappushpop(heap, (-pair_sum, [nums1[i], nums2[j]]))
                else:
                    break
        
        while heap:
            ans.append(heapq.heappop(heap)[1])
        
        return ans

# TC : O(n1 * n2 + k log k) where n1 is length of nums1 and n2 is the lenght of nums2
# SC : O(k)