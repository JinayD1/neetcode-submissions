class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # compute minimum value running total
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            elif(prices[r] - prices[l] > maxProfit):
                maxProfit = prices[r] - prices[l]
            r += 1
        return maxProfit