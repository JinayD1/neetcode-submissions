class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize both pointers to start of list
        buy = [0, prices[0]]
        sell = [0, prices[0]]
        max_profit = 0

        # create loop to go through price index
        for i in range(len(prices)):

            # check if current price is less than our buy
            if prices[i] < buy[1]:
                buy = [i, prices[i]]
                sell = [i, prices[i]]
            elif prices[i] > sell[1]:
                sell = [i, prices[i]]
            if sell[1] - buy[1] > max_profit:
                max_profit = sell[1] - buy[1]
            
        return max_profit
        
        # need to build running total of profit