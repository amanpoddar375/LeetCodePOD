class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(1,n):
            for j in range(i):
                d = nums[i]-nums[j]
                s = 0
                if d in dp[j]:
                    s =  dp[j][d]
                dp[i][d] += s +1
                res += s
        return res