class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        xd = abs(sx-fx)
        yd = abs(sy-fy)

        # calculate the diagonal distance (minimum of x and y differences)
        didist = min(xd,yd)

        # subtract the diagonal distance from the remaining x and y differences
        xd -= didist
        yd -= didist

        total_dist = didist + xd + yd

        # if the total distance is zero, it means the start and end positions are the same
        # In this case, it's only possible to reach the same cell if there is more than 1 second available (t != 1)
        if total_dist == 0:
            return t != 1
        return total_dist <= t
    
# TC : O(1)
# SC : O(1)