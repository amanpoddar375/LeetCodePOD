class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for u, v in connections:
            graph[u].append((v, 1))     #forward edge
            graph[v].append((u, 0))     #backward edge

        visited = [False] * n
        count = [0]

        def dfs(node):
            visited[node] = True
            for neighbor, is_forward in graph[node]:
                if not visited[neighbor]:
                    #if this edge is in forward direction, we need to change it
                    if is_forward:
                        count[0] += is_forward
                    dfs(neighbor)

        dfs(0)
        return count[0]
# TC : O(n)
# SC : O(n), where n is the number of cities, to store the graph and visited arra
