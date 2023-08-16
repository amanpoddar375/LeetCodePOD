class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            window = nums[i:i+k]  
            max_in_window = max(window)  
            result.append(max_in_window)  

        return result


# TC : O(n*k), where n is the length of the input array nums and k is the window size
# SC : O(n)