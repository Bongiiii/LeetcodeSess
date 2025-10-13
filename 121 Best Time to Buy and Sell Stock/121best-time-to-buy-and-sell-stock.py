class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyn, maxProf = float('inf'),0

        for price in prices:
            buyn = min(price, buyn)
            maxProf = max(maxProf, price - buyn)

        return maxProf