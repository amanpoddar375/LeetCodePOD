class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        class UnionFind:
            def __init__(self, n):
                self.rank = [1] * n
                self.f = list(range(n))
                
            def find(self, x):
                if x == self.f[x]:
                    return x
                else:
                    self.f[x] = self.find(self.f[x])
                    return self.f[x]
                
            def union(self, x, y):
                fx = self.find(x)
                fy = self.find(y)
                if fx == fy:
                    return
                if self.rank[fx] > self.rank[fy]:
                    fx, fy = fy, fx
                self.f[fx] = fy
                if self.rank[fx] == self.rank[fy]:
                    self.rank[fy] += 1
        
        def get_mst(n, edges, blockedge, pre_edge = -1):
            uf = UnionFind(n)
            weight = 0
            if pre_edge != -1:
                weight += edges[pre_edge][2]
                uf.union(edges[pre_edge][0], edges[pre_edge][1])
            for i in range(len(edges)):
                if i == blockedge:
                    continue
                edge = edges[i]
                if uf.find(edge[0]) == uf.find(edge[1]):
                    continue
                uf.union(edge[0], edge[1])
                weight += edge[2]
            for i in range(n):
                if uf.find(i) != uf.find(0):
                    return 10**9 + 7
            return weight
        
        for i in range(len(edges)):
            edges[i].append(i)
            
        edges.sort(key=lambda x: x[2])
        origin_mst = get_mst(n, edges, -1)
        
        critical = []
        non_critical = []
        
        for i in range(len(edges)):
            if origin_mst < get_mst(n, edges, i):
                critical.append(edges[i][3])
            elif origin_mst == get_mst(n, edges, -1, i):
                non_critical.append(edges[i][3])
        
        return [critical, non_critical]

# TC : O(E * log(E)), where E is the number of edges.
# SC :  O(E).