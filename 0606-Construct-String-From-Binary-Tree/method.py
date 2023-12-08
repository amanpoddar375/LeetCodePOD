# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return ""

            result = str(node.val)

            if node.left or node.right:
                result += "(" + preorder(node.left) + ")"
            if node.right:
                result += "(" + preorder(node.right) + ")"

            return result

        return preorder(root)
    
# TC : O(n), where n is the number of nodes in the binary tree
# SC : O(h) or O(log n) in the average case, O(n) in the worst case