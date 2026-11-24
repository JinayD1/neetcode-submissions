class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIndex = 0
        sellIndex = 0
        profit = 0
        while (sellIndex < len(prices)):
            if (prices[sellIndex] <= prices[buyIndex]):    
                buyIndex = sellIndex

            newProfit = prices[sellIndex] - prices[buyIndex]
            if (profit < newProfit): 
                profit = newProfit
            sellIndex += 1
        return profit