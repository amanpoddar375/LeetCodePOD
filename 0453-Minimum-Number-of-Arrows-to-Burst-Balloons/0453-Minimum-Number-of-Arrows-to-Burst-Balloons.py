class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        endpoint = float("inf")
        points.sort()
        for start, end in points:
            if endpoint < start:
                ans += 1 
                endpoint = end
            else:
                endpoint = min(endpoint, end)
        return ans
      
# TC : O(nlogn), where n is the number of balloons. ( O(nlogn) + O(n) ): sorting function and for iteration through sorted list of balloons
# SC : O(1), since the solution does not use any additional space beyond the input array.
