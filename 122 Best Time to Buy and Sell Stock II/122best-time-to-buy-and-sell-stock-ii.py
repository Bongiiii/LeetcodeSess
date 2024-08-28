class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices or len(prices) == 1:
        #     return 0

        # profit, buyn = 0 , float('inf')
        # for price in prices:
        #     buyn = min(buyn, price)
        #     profit = max(profit, price - buyn)

        # return profit
    
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit