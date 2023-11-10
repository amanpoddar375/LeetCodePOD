class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        
        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break
        
        n = len(adjacentPairs) + 1
        result = [0] * n
        result[0] = start
        
        for i in range(1, n):
            result[i] = graph[result[i-1]].pop()
            graph[result[i]].remove(result[i-1])
        
        return result