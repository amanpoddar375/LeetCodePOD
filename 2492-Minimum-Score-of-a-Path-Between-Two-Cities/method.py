class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w       
        min_score = float('inf')
        visited = set()
        queue = deque([1])
        while queue:
            node = queue.popleft()
            for adj, score in graph[node].items():
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                min_score = min(min_score, score)           
        return min_score

# TC : O(V+E), where E is the number of edges in the input list roads and V is the number of vertices in the graph.

# SC : O(V+E) 
