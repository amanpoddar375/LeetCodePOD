class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # Function to check if two strings are similar
        def isSimilar(s1, s2):
            d = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    d += 1
                    if d > 2:
                        return False
            return True
        # DFS function to traverse the connected group of similar strings
        def dfs(s, visited, graph):
            visited.add(s)
            for neigh in graph[s]:
                if neigh not in visited:
                    dfs(neigh, visited, graph)
        n = len(strs) 
        # Construct graph with similar strings as edges
        graph = {s: [] for s in strs}
        for i in range(n):
            for j in range(i+1, n):
                if isSimilar(strs[i], strs[j]):
                    graph[strs[i]].append(strs[j])
                    graph[strs[j]].append(strs[i])
        # DFS to count the number of connected groups
        visited = set()
        count = 0
        for s in strs:
            if s not in visited:
                count += 1
                dfs(s, visited, graph)
        return count

# TC: O(n^2*k), where n is the number of strings in the input list and k is the maximum length of a string. 
# SC: O(n*k), for the graph and visited set.
