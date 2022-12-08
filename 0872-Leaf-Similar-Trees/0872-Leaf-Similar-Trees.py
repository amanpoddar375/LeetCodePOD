# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, v):
        if not root:
            return
        if not root.left and not root.right:
            v.append(root.val)
        self.dfs(root.left,v)
        self.dfs(root.right,v)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        self.dfs(root1, tree1)
        self.dfs(root2, tree2)
        return tree1 == tree2
