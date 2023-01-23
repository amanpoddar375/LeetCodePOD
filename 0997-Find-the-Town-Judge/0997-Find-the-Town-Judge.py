class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts, trustedby = defaultdict(int), defaultdict(int)
        for i,j in trust:
            trusts[i] -= 1
            trustedby[j] += 1
        for a in range(1, n+1):
            if trusts[a] == 0 and trustedby[a] == n-1:
                return a
        return -1
      
## TC : O(n)
## SC : O(n)
