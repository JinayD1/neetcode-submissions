class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            maxP = max(prices[r] - prices[l], maxP)
        
        return maxP