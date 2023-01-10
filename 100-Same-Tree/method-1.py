# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q

## TC: O(n), where n is the number of nodes in the tree. This is because we need to visit each node in the tree at least once to compare their values.

## SC : O(n), as the maximum space used by the recursion stack would be the height of the tree, which is O(n) in the worst case for a tree that is not balanced.

##Note: In the best case (when the tree is balanced), SC would be O(logn).
