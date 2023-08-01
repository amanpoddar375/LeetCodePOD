from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1),k))
    
# TC : O(C(n, k)), "C(n, k)" or "n choose k," and its formula is C(n, k) = n! / (k! * (n - k)!).
 
# SC : O(C(n, k))