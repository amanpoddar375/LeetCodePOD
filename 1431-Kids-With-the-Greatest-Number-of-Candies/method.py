class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for c in candies:
            if c + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
# TC : O(n), where n is the length of the candies list.
# SC : O(n)
