class Solution:
    def numTrees(self, n: int) -> int:
        """
        Understand:
        input - integer, output - integer
         edge-case: empty tree, given n = 0
        Match:
        dynamic programming
        recursion

        Plan:
        initialize a dp array of size n+1 to cater for the edge case, empty array even though constraints handled it
        base case, there is only one way of arranging 0 nodes
        iterate from 1 to n nodes inclusive and be checking for unique bst that can be made
        bst rules: left nodes are less than the root while the right nodes are also greater than the root, and the children are also bst
        finally return the last recorded number/ element in the dp array

        R/E:
        s/c = O(N), size of dp array
        t/c = O(N^2)
        """

        dp = [0] * (n+1)
        #set the first element in dp array to 1, base case/edge case
        dp[0] = 1

        for node in range(1, n+1):
            for leftTree in range(node):
                dp[node] += dp[leftTree] * dp[node - leftTree - 1]

        return dp[-1]