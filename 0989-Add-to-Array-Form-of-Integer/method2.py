class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        integer = int(''.join(map(str, num)))
        res = list(str(integer+ k))
        return [int(x) for x in res]
