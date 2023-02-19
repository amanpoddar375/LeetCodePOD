# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        if not root:
            return ans
        q.append(root)
        flag = False
        while q:
            size = len(q)
            level = []
            for i in range(size):
                temp = q.popleft()
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)     
                if temp.right:
                    q.append(temp.right)
            if flag:
                level.reverse()
            flag = not flag
            ans.append(level)
        return ans
      
 ''' TC : O(nlog(n)) i.e the code visits each node in the binary tree exactly once, so the TC is O(n), 
where n is the number of nodes in the tree. And, the  the TC of the inner loop is O(log(n))'''

''' SC : O(n) '''
