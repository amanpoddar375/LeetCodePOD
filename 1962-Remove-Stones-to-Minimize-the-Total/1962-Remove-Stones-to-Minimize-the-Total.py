class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        for i in range(k):
            largest_pile = heapq.heappop(heap)
            new_pile = largest_pile // 2
            heapq.heappush(heap, new_pile)
        total_stones = -sum(heap)
        return total_stones

#TC: O(n log n), where n is the number of piles, since we need to perform heap operations on each pile. 
#SC: O(n), since we need to store all the piles in the heap.
