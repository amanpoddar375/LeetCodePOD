class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1      
        ans = [[] for i in range(n)]        
        for u, v in connections:
            ans[u].append(v)
            ans[v].append(u)
        res, vis = 0, [0] * n
        def dfs(node, ans, vis):
            vis[node] = 1
            for k in ans[node]:
                if vis[k] == 0:
                    dfs(k, ans, vis)
        for i in range(n):
            if vis[i] == 0:
                res += 1
                dfs(i, ans, vis)
        return res - 1

'''# TC : O(n+m), where n is the number of computers and m is the number of connections in the input.
This is because the code performs a single pass over the connections to build the graph, and then 
performs a depth-first search (DFS) traversal over the graph to count the number of connected components.'''

'''# SC : O(n+m), since it creates an adjacency list representation of the graph and an array to keep track 
of visited nodes, both of which have a size proportional to n+m.'''
