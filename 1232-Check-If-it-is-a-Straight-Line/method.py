class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) <= 2:
            return True
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        if x1 -x0 != 0:
            slope = (y1 - y0)/(x1 - x0)
        else:
            slope = float('inf')

        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if xi - x0 != 0:
                curr_slope = (yi-y0)/(xi-x0)
            else:
                curr_slope = float('inf')

            if curr_slope != slope:
                return False

        return True
    
# TC : O(n), where n is the number of coordinates. 
# SC : O(1), the algorithm uses a constant amount of additional space to store variables.