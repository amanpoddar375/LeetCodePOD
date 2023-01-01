class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_factors = set()
        for x in nums:
            while x % 2 == 0:
                prime_factors.add(2)
                x = x // 2
            i = 3
            while x != 1:
                while x % i == 0:
                    prime_factors.add(i)
                    x = x // i
                i = i + 2
        return len(prime_factors)
      
  ''' TC: O(n * m), where n is the length of the list nums and m is the maximum number of times 
  we need to divide the largest number in nums by 2 before it becomes odd. 
  This is because the outer for loop iterates through all the elements in nums, 
  and the inner while loop has a worst-case time complexity of O(m) 
  because it continues dividing the number by 2 until it becomes odd. '''
  
  ''' SC : O(n), because we are creating a set to store the distinct prime factors of all the numbers in nums, 
  which takes up n space in memory. '''
