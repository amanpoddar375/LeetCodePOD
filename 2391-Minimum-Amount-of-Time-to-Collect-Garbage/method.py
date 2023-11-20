class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        last = {c: i for i, pgm in enumerate(A) for c in pgm}
        dis = list(accumulate(travel, initial=0))
        return len(''.join(A)) + sum(dis[last.get(c, 0)] for c in 'PGM')