class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrival_times = [(dist[i] + speed[i] - 1) // speed[i] for i in range(n)]
        arrival_times.sort()
        
        for i in range(n):
            if i >= arrival_times[i]:
                return i
        
        return n

# TC : O(nlogn)
# SC : O(n)