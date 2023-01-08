class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def findSlope(p, q):
            x1, y1 = p
            x2, y2 = q
            if x1 == x2:
                return 'inf'
            return (y1 - y2) / (x1 - x2)

        result = 1
        for i, p in enumerate(points):
            slopes = Counter()
            for q in points[i + 1:]:
                slope = findSlope(p, q)
                slopes[slope] += 1
                result = max(slopes[slope], result)
        return result + 1
