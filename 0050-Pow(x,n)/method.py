class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            return 1.0/self.myPow(x,-n)
        elif n%2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x* self.myPow(x*x, (n-1)//2)
        
# TC : O(nlogn), with each recursive call, the value of n is halved (or reduced significantly), 
# and the function makes only a logarithmic number of recursive calls to reach the base case where n becomes 0.

# SC : O(nlogn), due to the recursive calls that are stored on the call stack. 
# Since the maximum depth of the recursion is logarithmic to n