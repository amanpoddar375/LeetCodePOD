class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(0, n):
            lcmi = nums[i]
            for j in range(i, n):
                #using built-in function lcm(a,b)
                lcmi = lcm(lcmi, nums[j])
                #as long as lcm will be equal to k , it will find out the subarrays
                #and if lcm will be greater than k , it won't work
                if (lcmi ==k): 
                    count = count +1
        return count