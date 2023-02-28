# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(int)
        ans = []
        def preorder(node):
            if not node:
                return "null"
            s = ",".join([str(node.val), preorder(node.left), preorder(node.right)])
            subtrees[s] += 1
            if subtrees[s] == 2:
                ans.append(node)
            return s
        
        preorder(root)
        return ans
