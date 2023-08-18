class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        city_connections = [0] * n  # To count the number of connections for each city
        connected = set()  # To keep track of direct connections
        
        for road in roads:
            city_connections[road[0]] += 1
            city_connections[road[1]] += 1
            connected.add((road[0], road[1]))
            connected.add((road[1], road[0]))
        
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate network rank for pair (i, j)
                rank = city_connections[i] + city_connections[j]
                # If there's a direct connection between i and j, we need to subtract 1 from rank
                if (i, j) in connected:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank

# TC : O(r + n^2). where is the number of roads and n is the number of cities
# SC : O(n)