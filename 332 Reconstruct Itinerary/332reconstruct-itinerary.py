from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        U:
        input - array of array of strings, output - array of strings
        -- we are not looking for the shortest path, but the path that uses all tickets in the smallest alphabetic order

        M:
        graph
        dfs with a backtrack approach

        P:
        build an adjacency list and add the data from input after reverse
         sorting them to make it easier for attaining alphabetic order
        then dfs method that checks if from start point you can move and remove match from stack 
        I:
        R/E:

        """
        map = defaultdict(list)
        
        #iterate through the input in reverse order
        for fro, to in sorted(tickets, reverse=True):
            map[fro].append(to)


        #dfs helper
        def dfs(start):
            while map[start]:
                dfs(map[start].pop())

            res.append(start)


        #calling it on our input list starting at jfk
        #stack to store results
        res = []

        dfs("JFK")

        return res[::-1]