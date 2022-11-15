class Solution:
        # @param {TreeNode} root
        # @return {integer}
        def leftheight(self, node):
            height = 0
            while(node):
                height = height +1
                node = node.left
            return height
        
        def rightheight(self, node):
            height = 0
            while(node):
                height = height +1
                node = node.right
            return height
        def countNodes(self, root):
            if(root == 0):
                return 0
            lh = self.leftheight(root)
            rh = self.rightheight(root)
            if(lh == rh):
                return pow(2,lh)-1
            else:
                return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
