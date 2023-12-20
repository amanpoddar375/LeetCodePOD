class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        n = len(prices)
        min_diff = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                total_price = prices[i] + prices[j]
                rem = money - total_price
                if total_price < min_diff:
                    min_diff = total_price
        
        return money - min_diff if min_diff <= money else money