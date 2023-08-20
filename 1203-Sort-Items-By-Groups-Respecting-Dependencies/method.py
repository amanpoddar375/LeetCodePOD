
class Solution:
    def topologicalSort(self, vertices, edges):
        n = len(vertices)
        out_edges = [[] for _ in range(n)]
        in_deg = [0] * n
        for i, j in edges:
            out_edges[i].append(j)
            in_deg[j] += 1

        inds = [i for i in range(n) if in_deg[i] == 0]
        for i in inds:
            for j in out_edges[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    inds.append(j)
        if len(inds) == n:
            return [vertices[i] for i in inds]
        raise RuntimeError

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = [[] for _ in range(m)]
        intra_lookup = [{} for _ in range(m)]
        for i in range(n):
            if group[i] == -1:
                intra_lookup.append({i: 0})
                groups.append([i])
            else:
                g = group[i]
                intra_lookup[g][i] = len(groups[g])
                groups[g].append(i)
        intra_lookup = [g for i, g in enumerate(intra_lookup) if groups[i]]
        groups = [g for g in groups if g]
        m = len(groups)

        inter_lookup = [None] * n
        for g, ita in enumerate(intra_lookup):
            for i in ita:
                inter_lookup[i] = g

        inter_b, intra_b = [], [[]for _ in range(m)]
        for i, b in enumerate(beforeItems):
            gi = inter_lookup[i]
            for j in b:
                gj = inter_lookup[j]
                if gi == gj:
                    intra_b[gi].append([intra_lookup[gi][j], intra_lookup[gi][i]])
                else:
                    inter_b.append([gj, gi])

        try:
            groups = self.topologicalSort(list(zip(groups, intra_b)), inter_b)
            for g in range(m):
                groups[g] = self.topologicalSort(groups[g][0], groups[g][1])
            return sum(groups, [])
        except RuntimeError:
            return []


# TC : O(V + E + m + n), 
# where V is the number of vertices and E is the number of edges.
# where m is the length of groups, and n is the length of vertices.


# SC : O(V + E + m + n)