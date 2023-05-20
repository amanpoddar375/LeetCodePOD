class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}
        for (a, b), val in zip(equations, values):
            if a in graph:
                graph[a][b] = val
            else:
                graph[a] = {b: val}
            if b in graph:
                graph[b][a] = 1 / val
            else:
                graph[b] = {a: 1 / val}

        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0

            if src == dest:
                return 1.0
            visited.add(src)
            for neighbor in graph[src]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    value = dfs(neighbor, dest, visited)
                    if value != -1.0:
                        return graph[src][neighbor] * value
            return -1.0
        results = []
        for query in queries:
            src, dest = query
            results.append(dfs(src, dest, set()))

        return results

# TC : O(N + Q * (V + E)), where  N is the total s of equations, Q is the s of queries, V is the s of variables, and E is the s of edges (equations).
# SC : O(N + V)
