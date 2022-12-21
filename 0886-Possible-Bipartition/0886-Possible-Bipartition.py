class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i: [] for i in range(1, n+1)}
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colors = {i: 0 for i in range(1, n+1)}

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
                elif colors[neighbor] == color:
                    return False
            return True
        for node in range(1, n+1):
            if colors[node] == 0 and not dfs(node, 1):
                return False
        return True
