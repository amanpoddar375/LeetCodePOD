class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        totalsum = 0
        currentsum = 0
        n = len(nums)
        minsum = math.inf
        for i in range(n):
            totalsum += nums[i]
        for i in range(n):
            currentsum += nums[i]
            
            fpavg = currentsum
            fpavg//=(i+1)
            spavg = totalsum - currentsum
            if(i == n-1):
                if(fpavg<minsum):
                    return n-1
                else:
                    break
            spavg //= (n-i-1)
            diff = abs(fpavg -spavg)
            if(diff<minsum):
                minsum = diff
                answerIndex = i
        return answerIndex