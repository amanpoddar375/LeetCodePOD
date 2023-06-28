class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adj[u].append((v, p))
            adj[v].append((u, p))

        dist = [0.0] * n
        dist[start] = 1.0

        queue = deque([start])

        while queue:
            curr = queue.popleft()

            for node, prob in adj[curr]:
                new_prob = dist[curr] * prob

                if new_prob > dist[node]:
                    dist[node] = new_prob
                    queue.append(node)

        return dist[end]

# TC : O(m)
# SC : O(m + n), where n nodes and m edges.
