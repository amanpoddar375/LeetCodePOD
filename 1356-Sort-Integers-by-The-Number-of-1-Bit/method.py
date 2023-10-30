class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_ones(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        return sorted(arr, key=lambda x: (count_ones(x), x))
