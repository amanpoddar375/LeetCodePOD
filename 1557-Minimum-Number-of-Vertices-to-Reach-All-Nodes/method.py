class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inEdge = set()
        for edge in edges:
            inEdge.add(edge[1])
        result = []
        for i in range(n):
            if i not in inEdge:
                result.append(i)

        return result

# TC : O(E + n), where E is the number of edges in the graph, n is the number of nodes in the graph
# SC : O(E + n)
