class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalg, currg, startInd = 0, 0, 0
        for i in range(0, len(gas)):
            currg += gas[i] - cost[i]
            totalg += gas[i] - cost[i]
            if currg < 0:
                startInd = i + 1
                currg = 0
        return startInd if totalg >= 0 else -1
