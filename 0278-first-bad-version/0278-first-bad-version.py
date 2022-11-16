# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        l= 1
        h= n 
        while(l<h):
            m = (h+l)/2
            if isBadVersion(m):
                h = m
            else:
                l= m+1
        return int(l)