# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        if not root:
            return True
        return isMirror(root.left, root.right)

      # TC : O(n), where n is the number of nodes in the binary tree
      # SC : O(h), where h is the height of the tree. 
