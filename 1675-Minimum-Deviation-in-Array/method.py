class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_heap = []
        max_num = 0
        for num in nums:
            temp = num
            while num % 2 == 0:
                num //= 2    
            min_heap.append((num, max(temp, num * 2)))
            max_num = max(max_num, num)
        
        min_deviation = float("inf")
        heapq.heapify(min_heap)
        while len(min_heap) == len(nums):
            num, num_max = heapq.heappop(min_heap)
            min_deviation = min(min_deviation, max_num - num)

            if num < num_max:
                heapq.heappush(min_heap, (num * 2, num_max))
                max_num = max(max_num, num * 2)
        return min_deviation
      
      
''' TC : the time complexity of the solution should be O(nlogm*logn), where m is the maximum value after any number of operations. 
This is because the while loop that performs the operations has a maximum of logm iterations, and each iteration involves 
a heap operation which takes logn time.
In the worst case where all the elements in the array are odd and the maximum value after any number of operations is 2^k times the minimum element, 
the value of m is 2^knums[0], and the time complexity becomes O(nlog(2^knums[0])logn) = O(nklogn). 
However, since k is bounded by the maximum number of times we can double an odd number to get an even number, which is log2(10^9) = 30, 
the time complexity is effectively O(nlogn).'''

''' SC: O(n), where n is the length of the input list nums. This is because we create a min heap to store tuples of values, 
and the size of the heap can be at most equal to the length of the input list. 
Additionally, we use a few extra variables that do not depend on the size of the input, 
so their contribution to the overall space complexity is negligible. '''
