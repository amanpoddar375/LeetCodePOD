class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        all_paths = []
        def dfs(node, path):
            if node == n - 1:
                all_paths.append(path)
                return
            for neighbor in graph[node]:
                dfs(neighbor, path + [neighbor])
        dfs(0, [0])
        return all_paths
#TC: O(V + E), where V is the number of vertices (nodes) in the graph and E is the number of edges.
#SC: O(V + E), since the list of all paths and the current path passed to the recursive function both have length at most V + E.
