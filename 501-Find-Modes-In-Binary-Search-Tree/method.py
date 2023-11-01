# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTraversal(node):
            if not node:
                return []
            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right)

        if not root:
            return []

        values = inOrderTraversal(root)
        counts = {}
        max_count = 0
        modes = []

        for val in values:
            counts[val] = counts.get(val, 0) + 1
            max_count = max(max_count, counts[val])

        for val, count in counts.items():
            if count == max_count:
                modes.append(val)

        return modes
