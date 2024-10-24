class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Understand:
        input - array, integer and output - integer

        Match:
        array
        math
        dp

        Plan:
        based on the constraints, there wont be a coin of value 0 and less
        use a dp array of size amount + 1
        we know there is only one way of making 0 change
        iterate for each coin and also check for each val within that range and see if we can make 

        R/E:
        s/c = O(N), n= amount + 1
        t/c = O(C*A)
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(1,amount+1):
                if coin <= x:
                    dp[x] += dp[x - coin]
                else:
                    continue

        return dp[-1] 