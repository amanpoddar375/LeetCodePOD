class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ''' winners, losers, table = [], [], {}
        for winner, loser in matches:
            # map[key] = map.get(key, 0) + change . This format ensures that KEY NOT FOUND error is always prevented.
            # map.get(key, 0) returns map[key] if key exists and 0 if it does not.
            table[winner] = table.get(winner, 0)  # Winner
            table[loser] = table.get(loser, 0) + 1
        for k, v in table.items(): # Player k with losses v
            if v == 0:
                winners.append(k) # If player k has no loss ie v == 0
            if v == 1:
                losers.append(k) # If player k has one loss ie v == 1
        return [sorted(winners), sorted(losers)] # Problem asked to return sorted arrays.'''
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]
        winnerWithZeroLose = list(set(winners) - set(losers))
        loserCount = collections.Counter(losers)
        atleastonelost = []
        for loser in loserCount:
            if loserCount[loser] == 1:
                atleastonelost.append(loser)
        return [sorted(winnerWithZeroLose), sorted(atleastonelost)]