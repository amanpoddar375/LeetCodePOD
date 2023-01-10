# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        
        return True

## TC: O(n), where n is the number of nodes in the tree. as we need to visit each node in the tree at least once.

## SC : O(n),as the maximum space used is proportional to the number of nodes in the tree

##Note: This iterative solution is more efficient than the recursive solution in terms of SC, as it does not use recursion stack space.
