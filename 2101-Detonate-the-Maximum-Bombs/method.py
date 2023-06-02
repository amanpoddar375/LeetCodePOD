class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        max_bombs = 0
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i].append(j)

        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            max_bombs = max(max_bombs, len(visited))

        return max_bombs
