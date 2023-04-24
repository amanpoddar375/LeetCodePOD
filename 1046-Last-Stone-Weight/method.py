class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-s for s in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, -(y-x))       
        return -pq[0] if pq else 0
'''TC : O(n log n), where n is the length of the input array 'stones'. 
This is because creating a priority queue takes O(n) time, and each operation of 
inserting or extracting elements from the priority queue takes O(log n) time.

SC : O(n), because we are storing all elements of the input array in the priority queue. '''
