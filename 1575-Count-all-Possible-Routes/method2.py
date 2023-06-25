class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(current_city: int, remaining_fuel: int) -> int:
            if remaining_fuel < 0:
                return 0
            else:
                if current_city == finish:
                    result = 1
                else:
                    result = 0
            for next_city in range(len(locations)):
                if current_city != next_city:
                    cost = abs(locations[current_city] - locations[next_city])
                    result += dfs(next_city, remaining_fuel - cost)
            return result % MOD
        
        return dfs(start, fuel)
    
# TC : O(N * F),the dfs function is memoized using the lru_cache decorator, which ensures that each unique function call is computed only once. 
# SC : O(N * F)


