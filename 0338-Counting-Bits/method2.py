class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0,n+1):
            count_ones = bin(i).count('1')
            ans.append(count_ones)
        return ans
        
# TC: O(nlogn)
# SC: O(n)