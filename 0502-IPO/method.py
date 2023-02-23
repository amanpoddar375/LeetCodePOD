class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapify(minCapital)
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heappop(minCapital)
                heappush(maxProfit, -p)
            if not maxProfit:
                break
            w -= heappop(maxProfit)
        return w

# TC : O(nlogn), where n is the number of projects
# SC : O(n)
