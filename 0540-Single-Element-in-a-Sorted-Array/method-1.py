#Stack Implementation
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if ans and ans[-1] == num:
                ans.pop()
            else:
                ans.append(num)
        return ans[0]
# TC : O(n)
# SC : O(n)
