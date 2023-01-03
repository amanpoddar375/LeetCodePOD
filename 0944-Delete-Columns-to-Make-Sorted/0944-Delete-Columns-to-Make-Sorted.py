class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        length = len(strs[0])
        for col in range(length):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    count+=1
                    break
        return count
# TC : O(m*n), where n is the number of strings and m is the length of the strings.
# SC : O(1), as we only use a constant amount of space regardless of the input size.
