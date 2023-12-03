class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        def calculate_time(point1, point2):
            x_diff = abs(point2[0] - point1[0])
            y_diff = abs(point2[1] - point1[1])
            return max(x_diff, y_diff)
        
        total_time = 0
        for i in range(1, len(points)):
            total_time += calculate_time(points[i-1], points[i])
        
        return total_time
