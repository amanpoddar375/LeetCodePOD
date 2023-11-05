class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        if k >= len(arr) - 1:
            return max_num
        wins = 0
        current_winner = arr[0]
        
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                wins += 1
            else:
                current_winner = arr[i]
                wins = 1
            if wins == k:
                return current_winner
        
        return max_num