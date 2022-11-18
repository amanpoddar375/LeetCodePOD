class Solution:
    def isUgly(self, n: int) -> bool:
        d = [2, 3, 5]
        if(n<=0):
            return False
        for i in d :
            while n % i == 0 :
                n /= i
        return n==1