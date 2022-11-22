class Solution:
    def numSquares(self, n: int) -> int:
        if(ceil(sqrt(n))==floor(sqrt(n))): return 1
        while(n%4 == 0): n//=4
        if(n%8==7): return 4
        i =1
        while(i*i <=n):
            b = floor(sqrt(n-i*i))
            if(b*b == n- i*i): return 2
            i=i+1 
        return 3