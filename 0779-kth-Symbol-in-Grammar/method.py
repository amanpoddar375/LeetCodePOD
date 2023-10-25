class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        mid = 2 ** (n - 2)
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)

# TC : O(N), where N is the row number n
# SC : O(N) as well, as it incurs a recursive call stack of depth N.