class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
            for i in range(2, n + 1):
                if primes[i]:
                    for j in range(i * 2, n + 1, i):
                        primes[j] = False
            return primes
        primes = sieve(right)
        ans = [-1, -1]
        min_diff = float('inf')
        last_prime = -1
        for i in range(left, right + 1):
            if primes[i]:
                if last_prime != -1:
                    diff = i - last_prime
                    if diff < min_diff:
                        min_diff = diff
                        ans = [last_prime, i]
                last_prime = i
        return ans
      
 ''' TC : O(n * log(n)), where n is the range right - left + 1. This is 
 because the Sieve of Eratosthenes algorithm has a TC of O(n * log(n)) 
 for generating a list of prime numbers up to n, and the function iterates 
 through the range left to right once, which takes O(n) time. '''

''' SC : O(n), as the function uses an array of size n to store the list of prime numbers. '''
