class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()
        
        for i in range(len(nums)):
            while window and window[0] < i - k + 1:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)
            
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result

# TC : O(n), where n is the length of the input array nums
# SC : O(k), where k is the window size