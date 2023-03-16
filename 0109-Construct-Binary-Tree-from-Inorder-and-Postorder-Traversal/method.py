# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorder_idx = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorder_idx+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_idx], postorder)

        return root

''' TC : O(n^2), where n is the number of nodes in the binary tree. because the index() function has TC O(n) when searching for an element in a list. 
The function is called twice for each node in the tree, once to find the inorder index and once to check if the inorder and postorder lists are empty.'''
''' SC : O(n), because the function uses recursive calls to build the tree, which can result in a call stack of size n in the worst case, if the tree is skewed.'''
