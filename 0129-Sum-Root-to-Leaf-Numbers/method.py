# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, sum):
            if not node:
                return 0
            sum = sum * 10 + node.val
            if not node.left and not node.right:
                return sum
            return dfs(node.left, sum) + dfs(node.right, sum)
        return dfs(root, 0)  

# TC : O(n), where n is the number of nodes in the binary tree.
# SC : O(h), where h is the height of the binary tree
