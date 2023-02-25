class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

''' TC: O(n), where n is the length of the prices list. This is because we loop through the list once, 
performing a constant amount of work for each element.'''

''' SC: O(1). We only use a constant amount of extra space to store min_price and max_profit, regardless of the size of the input.'''
