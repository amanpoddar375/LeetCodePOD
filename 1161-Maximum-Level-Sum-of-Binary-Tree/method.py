class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0

        current_level = [root]
        max_level = 1
        max_sum = float('-inf')
        level = 1

        while current_level:
            level_sum = 0
            next_level = []

            for node in current_level:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            current_level = next_level
            level += 1

        return max_level

# TC : O(n)
# SC : O(n)