class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #sort costs based on the greedy approach of minimizing cost
        costs.sort(key=lambda x:x[0]-x[1])

        #bit shit/ divide by 2 to find n people
        n = len(costs) >> 1

        return sum(costs[i][0] + costs[i+n][1] for i in range(n))