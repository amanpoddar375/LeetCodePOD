# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
    
# TC : O(n), where n is the number of nodes in the binary tree.
# SC : O(h) or O(log n) in the average case, O(n) in the worst case