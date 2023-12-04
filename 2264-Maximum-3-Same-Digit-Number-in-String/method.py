class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        maxi = ""
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                curr= num[i:i + 3]
                maxi = max(maxi, curr)

        return 

# TC : O(N), where N is the length of the input string num. 
# SC : O(1)