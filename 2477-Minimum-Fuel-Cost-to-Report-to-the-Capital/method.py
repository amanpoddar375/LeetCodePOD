class Solution:
    def minimumFuelCost(self, roads, seats):
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        self.min_fuel_cost = 0
        def calculateFuelCost(city, parent, passengers=1):
            for neighbor in graph[city]:
                if neighbor == parent:
                    continue
                passengers += calculateFuelCost(neighbor, city)
            trips = int(ceil(passengers / seats))
            self.min_fuel_cost += (trips if city else 0)
            return passengers
        calculateFuelCost(0, 0)
        return self.min_fuel_cost
