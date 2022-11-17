class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        a = max(min(x2,x4) > max(x1,x3),0)
        b = max(min(y2,y4) > max(y1,y3), 0)
        return a * b > 0