# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root, maxN, minN):
        if not root:
            return abs(maxN - minN)
        maxN = max(root.val, maxN)
        minN = min(root.val, minN)
        left = self.find(root.left, maxN, minN)
        right = self.find(root.right, maxN, minN)
        return max(left, right)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.find(root, root.val, root.val)
