class Solution:
    def signFunc(self, x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return self.signFunc(product)

      # TC : O(n)
      # SC : O(1)
