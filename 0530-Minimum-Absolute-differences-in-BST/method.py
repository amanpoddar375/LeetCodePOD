# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        values = inorder(root)
        min_diff = float('inf')
        for i in range(1,len(values)):
            diff = abs(values[i]- values[i-1])
            min_diff = min(diff,min_diff)
        
        return min_diff

# TC : O(n), where n is the number of nodes in BST
# SC : O(n)