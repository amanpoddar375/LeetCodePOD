class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        total_sum = sum(rods)
        max_height = [-1] * (total_sum + 1)
        max_height[0] = 0

        for rod_length in rods:
            dp = max_height[:]

            for i in range(total_sum - rod_length + 1):
                if dp[i] < 0:
                    continue

                max_height[i + rod_length] = max(max_height[i + rod_length], dp[i])
                max_height[abs(i - rod_length)] = max(max_height[abs(i - rod_length)], dp[i] + min(i, rod_length))

        return max_height[0]

# TC : O(N * S), where N is the number of rods and S is the sum of all rod lengths. 
# SC : O(S), where S is the sum of all rod lengths.