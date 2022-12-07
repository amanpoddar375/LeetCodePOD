# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high, 0)
    def dfs(self, root, low, high,sum):
        if not root:
            return sum
        if low <= root.val <= high:
            sum += root.val
        sum = self.dfs(root.left, low, high, sum)
        sum = self.dfs(root.right, low, high, sum)
        return sum
