class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            j = stack[-1] if stack else -1
            ans[i] = ans[j] + (i-j) * arr[i]
            
            stack.append(i)
            
        return sum(ans) % (10**9+7)