# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        flag = False
        while q:
            node = q.popleft()
            if node is None:
                flag = True
            else:
                if flag:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True

# TC : O(n), where n is the number of nodes in the binary tree, as we visit every node in the worst case.

# SC : O(n/2), which is the maximum number of nodes that can be present in the last level of a complete binary tree.
