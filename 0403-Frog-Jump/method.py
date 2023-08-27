class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        stone_positions = set(stones)
        jump_dict = {stone: set() for stone in stones}
        jump_dict[0].add(0)  
        
        for stone in stones:
            for jump in jump_dict[stone]:
                for step in range(jump - 1, jump + 2):
                    if step > 0 and stone + step in stone_positions:
                        jump_dict[stone + step].add(step)
        
        return bool(jump_dict[stones[-1]])


# TC : O(n^2), where n is the number of stones
# SC : O(n), because of use of jump_dict dictionary