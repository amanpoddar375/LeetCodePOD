"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build_quad_tree(size, row, col):
            # If the size of the grid is 1, create a leaf node with the grid value
            if size == 1:
                return Node(grid[row][col], True, None, None, None, None)

            # Check if all elements in the grid have the same value
            all_same = True
            for i in range(size):
                for j in range(size):
                    if grid[row+i][col+j] != grid[row][col]:
                        all_same = False
                        break
                if not all_same:
                    break

            # If all elements have the same value, create a leaf node
            if all_same:
                return Node(grid[row][col], True, None, None, None, None)

            # Otherwise, divide the grid into four quadrants and recursively build the quad tree
            half_size = size // 2
            topLeft = build_quad_tree(half_size, row, col)
            topRight = build_quad_tree(half_size, row, col+half_size)
            bottomLeft = build_quad_tree(half_size, row+half_size, col)
            bottomRight = build_quad_tree(half_size, row+half_size, col+half_size)
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        # Call the recursive function with the full size of the grid and starting at (0, 0)
        return build_quad_tree(len(grid), 0, 0)
      
      
''' TC : O(n^2 logn)'''
''' SC : O(n^2 logn)'''
