class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)  # Extra space for easier index handling
        max_side = 0
        prev = 0  # To keep track of the previous dp[i-1][j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == "1":
                    temp = dp[j]  # Store current dp[j] before updating
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    max_side = max(max_side, dp[j])
                    prev = temp  # Update prev for the next iteration
                else:
                    prev = dp[j]  # Update prev when matrix[i-1][j-1] is "0"
                    dp[j] = 0
        
        return max_side * max_side  # Return area
