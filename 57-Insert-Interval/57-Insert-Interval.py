class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for curr in intervals:
            if curr[1] < newInterval[0]:
                ans.append(curr)
            elif newInterval[1] < curr[0]:
                ans.append(newInterval)
                newInterval = curr
            else:
                newInterval[0] = min(curr[0], newInterval[0])
                newInterval[1] = max(curr[1], newInterval[1])
        ans.append(newInterval)
        return ans
      
## TC : O(n), where n is the number of intervals in the input list.
## SC : O(n). 
