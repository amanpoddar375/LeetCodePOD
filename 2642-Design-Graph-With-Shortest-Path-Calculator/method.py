class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adjList = defaultdict(list)
        for u,v,w in edges:
            self.adjList[u].append((v,w))

    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        self.adjList[u].append((v,w))
        
    # can't use dp since we are adding edges online
    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)] # distance, 
        
        dist = [inf] * self.n
        #dist[node1] = 0
        #visited = [False] * self.n
        
        while pq:
            d,i = heappop(pq)
            if d > dist[i]: continue
            #if visited[i]: continue
            #visited[i] = True
            
            if i == node2: return d
            
            for nbr,w in self.adjList[i]:
                if d + w < dist[nbr]:
                    dist[nbr] = d + w
                    heappush(pq, (dist[nbr], nbr))
            
        return -1