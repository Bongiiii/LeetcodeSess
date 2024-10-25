class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Understand:
        input - array, integer, and output - integer

        Match:
        array
        dp
        math

        Plan:
        iterate through the denominations/coins
        for each coin try to make change using the least amount of coins possible
        initiate a dp array of size amount + 1 and initialize all in the array to float('inf')
        the zero index element will be set to 0 
        then populate rest of the dp array using the coins
        iterate each coin and for each coin check if it is posible to use that coin and still have a remainder, and find the coins to use to breach the remainder gap
        update/fill dp array from [1:] using the minimum between the current element at that index and the previous dp address and also add the coin you are currently using to make change
        finally return the last element in the dp if it's not float('inf') else return -1 instead to show that the amount of money cannot be made from that combination

        R/E:
        s/c = O(N), n = amount + 1
        t/c = O(N*C), c = length of coins
        """
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1