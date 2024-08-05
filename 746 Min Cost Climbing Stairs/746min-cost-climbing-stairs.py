class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #using dp tabulation bottom up 
        # Manage edge case of 2 steps and under
        if len(cost) <= 2:
            return min(cost)
        
        # Reuse the cost array to build up to our answer
        for i in range(2, len(cost)):
            # From the given numbers we can build up to any number of number of steps
            # The minimum cost of step is the result of the current step and minimum between two previous steps
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
        
        # Return the minimum cost of climbing stairs by getting the minimum cost of last two steps
        return min(cost[i], cost[i-1])