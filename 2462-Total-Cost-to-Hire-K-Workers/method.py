class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = costs[:candidates] # Heap for the first candidates workers
        r = costs[max(candidates, len(costs) - candidates):] # Heap for the last candidates workers
        heapq.heapify(q)
        heapq.heapify(r)
        total_cost = 0
        i = candidates
        j = len(costs) - candidates - 1
        
        for _ in range(k):
            if not r or q and q[0] <= r[0]:  # Choose the worker with the lowest cost from q
                total_cost += heapq.heappop(q)
                if i <= j:
                    heapq.heappush(q, costs[i])  # Add the next worker from the remaining workers
                    i += 1
            else:  # Choose the worker with the lowest cost from r
                total_cost += heapq.heappop(r)
                if i <= j:
                    heapq.heappush(r, costs[j])  # Add the next worker from the remaining workers
                    j -= 1
        
        return total_cost


# TC :  O(n log n), where n is the length of the costs list.
# SC :  O(1), code uses a constant amount of extra space for variables, regardless of the input size. 