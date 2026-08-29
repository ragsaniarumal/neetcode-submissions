class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_price = prices[0]

        for price in prices:
            best_price = min(price, best_price)
            max_profit = max(max_profit, price - best_price)
        
        return max_profit
            