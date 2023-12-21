class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        x = [point[0] for point in points]
        x.sort()
        max_width = 0
        for i in range(1, len(x)):
            max_width = max(max_width, x[i] - x[i - 1])
        
        return max_width
