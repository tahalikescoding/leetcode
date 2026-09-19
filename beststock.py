#LEET CODE 121: BEST TIME TO BUY AND SELL STOCK

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        best = 0 
        for i in prices:
            min_price = min(min_price,i)
            profit = i-min_price
            best = max(best,profit)
        return best

