class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True

# TC : O(n log n), where n is the length of the input list.
# SC : O(1), as it only requires a few variables to store intermediate values and loop indices.