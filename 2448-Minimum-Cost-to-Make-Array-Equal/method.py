class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        left = 1
        right = 10**6
        min_cost = float('inf')
        
        # Binary search loop
        while left <= right:
            mid = (right - left) // 2 + left
            a = b = 0

            # Calculate costs a and b for the current mid value
            for i, num in enumerate(nums):
                a += abs(mid - num) * cost[i]
                b += abs(mid + 1 - num) * cost[i]

            # Update the minimum cost
            min_cost = min(a, b, min_cost) if min_cost is not None else min(a, b)

            # Update left and right based on a and b
            if b > a:
                right = mid - 1
            else:
                left = mid + 1

        return min_cost

# TC : The binary search algorithm has a TC of (log n), where n is the difference between right and left. 
# The inner loop iterates through the nums array, which takes O(n) time. Therefore, the overall TC is O(n log n).

# SC : O(1) since the algorithm only uses a constant amount of additional space to store variables.