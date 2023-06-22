class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        cash = 0  # Maximum profit with no stock in hand
        hold = -prices[0]  # Maximum profit with a stock in hand

        for i in range(1, n):
            prev_cash = cash
            cash = max(cash, hold + prices[i] - fee)  # Sell the stock
            hold = max(hold, prev_cash - prices[i])  # Buy the stock

        return cash

# TC : O(n), where n is the length of the prices array, as we iterate over the prices once.
# SC : O(1) since we only use a constant amount of additional space to store variables.
