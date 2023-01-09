#Method-I : Recursion

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        def preorder(node):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return result
## TC : O(n), where n is the number of nodes in the tree. This is because the function visits each node exactly once 
## SC : O(n), as the maximum size of the call stack will be n in the worst case    
      
#Method - II : Iterative method using Stack

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        if not root:
            return result
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)    
        return result
## TC : O(n), where n is the number of nodes in the tree. This is because the while loop iterates over all the nodes in the tree.
## SC : O(n), as the maximum size of the stack will be n in the worst case
