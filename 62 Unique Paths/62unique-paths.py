class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Understand:
        input - two integers (rows and columns of the grid)
        output - integer (number of unique paths)
        
        Match:
        - Dynamic Programming
        - Combinatorics
        
        Plan:
        - Create a DP table `dp[m][n]`, where `dp[i][j]` represents the number of unique paths to that cell.
        - Initialize `dp[0][j] = 1` for all `j` (only one way to move right).
        - Initialize `dp[i][0] = 1` for all `i` (only one way to move down).
        - Fill the DP table using:
          `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
        - Return `dp[m-1][n-1]` as the final result.

        R/E:
        - Time Complexity: O(m * n)
        - Space Complexity: O(m * n)
        """
        # Create DP table
        dp = [[1] * n for _ in range(m)]
        
        # Fill the DP table
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]
