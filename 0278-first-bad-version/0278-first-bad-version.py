# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        i=1
        j=n
        while i<j:
            k=(i+j)/2
            if isBadVersion(k):
                j=k
            else:
                i=k+1
        return int(i)