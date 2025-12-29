from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        U:
        input-array of arrays with lowercase letters for variables, and array of floats,
         another array of arrays with lowercase letters for variables to be queried
        output-an array of floats

        prob summary: given eqns, and values that satify the eqns, use the info to solve the queries provided.

        M:
        maths
        graph

        P:
        create a directed graph using the eqns and values

        I:
        R:
        E:
        """
        graph = defaultdict(list)

        #graph creation
        for i, [dividend, divisor] in enumerate(equations):
            graph[dividend].append((divisor, values[i]))
            graph[divisor].append((dividend, 1/values[i]))

        #helper function to divide
        def divisionHelper(dividend, divisor, visited):
            #base case when dividend and divisor are the same
            if dividend == divisor:
                return 1

            for new_divdnd, multiplier in graph[dividend]:
                if new_divdnd not in visited:
                    visited.add(new_divdnd)
                    ans = divisionHelper(new_divdnd, divisor, visited)
                    if ans > 0:
                        return ans * multiplier
                    visited.remove(new_divdnd)
                    
            return -1

        res = []
        for query in queries:
            dividend, divisor = query[0], query[1]
            # Check if BOTH variables exist in the graph first
            if dividend not in graph or divisor not in graph:
                res.append(-1)
            else:
                visited = set()
                visited.add(dividend)
                res.append(divisionHelper(dividend, divisor, visited))

        return res
