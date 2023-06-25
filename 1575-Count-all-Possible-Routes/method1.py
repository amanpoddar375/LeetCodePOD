class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        memo = {}

        def dfs(current_city: int, remaining_fuel: int) -> int:
            if (current_city, remaining_fuel) in memo:
                return memo[(current_city, remaining_fuel)]

            if remaining_fuel < 0:
                return 0
            else:
                if current_city == finish:
                    result =1 
                else:
                    result = 0
                      
            for next_city in range(len(locations)):
                if current_city != next_city:
                    cost = abs(locations[current_city] - locations[next_city])
                    result += dfs(next_city, remaining_fuel - cost)

            result %= MOD
            memo[(current_city, remaining_fuel)] = result
            return result
        
        return dfs(start, fuel)
    
# TC : O(N * F), number of cities as N and the maximum fuel as F.
# SC : O(N * F),  determined by the memoization dictionary memo. As we may need to store all N * F unique (current_city, remaining_fuel) pairs in the dictionary.