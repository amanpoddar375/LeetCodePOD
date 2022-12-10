# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = []
        def find(root):
            #base condition for a leaf node
            if not root: return 0
            sum = find(root.left) + find(root.right) + root.val
            #adding the possible sum of subtree into the stack ans
            ans.append(sum)
            return sum
        totalsum = find(root)
        #returning the max of products of sum of 2 subtress
        return int(max((totalsum-sum)*sum for sum in ans) % (1e9+7))
      
      #TC: O(n)
      #SC: O(h) 
