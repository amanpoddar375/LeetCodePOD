class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        paths = defaultdict(set)
        for start, end in edges:
            paths[start].add(end)
            paths[end].add(start)
        self.time = 0
        seen = set()
        def dfs(current):
            visited = False
            if current in seen:
                return
            seen.add(current)
            for next in paths[current]:
                if dfs(next):
                    visited = True
                    self.time += 2
            return visited or hasApple[current]
        dfs(0)
        return self.time

## TC : O(n), where n is the number of vertices in the tree, because each vertex is visited once.
## SC : O(n), where n is the number of vertices in the tree

'''It is also important to note that, the recursive function call also consumes O(H) extra space on the call stack, 
where H is the height of the tree. 
In the worst case, the height of a tree with N nodes is O(N) and on average case it is O(logN) for balanced tree. 
But as the solution is using set to keep track of visited vertices, the space complexity of the call stack is eliminated.'''
