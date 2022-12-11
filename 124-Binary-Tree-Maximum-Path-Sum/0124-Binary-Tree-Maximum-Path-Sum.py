# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self,root):
        if not root:
            return 0
        left = max(0, self.find(root.left))
        right = max(0, self.find(root.right))
        self.result = max(self.result, root.val + left + right)
        return max(left,right) + root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float('-inf')
        self.find(root)
        return self.result
