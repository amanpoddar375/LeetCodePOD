# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)  # sum, count

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                nonlocal result
                result += 1

            return total_sum, total_count

        result = 0
        dfs(root)
        return result
    
# TC : O(n), where n is the number of nodes in the binary tree    
# SC : O(H), where h is the height of the binary tree