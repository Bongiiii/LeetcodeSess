class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n, m = len(coins), amount

        #initiate a dp array that keeps the coins in index 0 and amount in index 1
        dp = [[float('inf')]*(m+1) for _ in range(n + 1)]
        dp[0][0] = 0

        for coin in range(1,n+1):
            curr_coin = coins[coin-1]

            for curr_amount in range(m + 1):
                #don't use curr coin
                dp[coin][curr_amount] = dp[coin - 1][curr_amount]

                #use current coin
                if curr_amount >= curr_coin:

                    #explore if you can use one more coin too
                    dp[coin][curr_amount] = min(dp[coin][curr_amount], dp[coin][curr_amount - curr_coin]+1)
        return -1 if dp[n][m] == float('inf') else dp[n][m]
