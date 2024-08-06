class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        dp = [[1]]  # Initialize the first row of Pascal's triangle

        for i in range(1, numRows):
            row = [1]  # Every row starts with 1
            for j in range(1, i):
                row.append(dp[i-1][j-1] + dp[i-1][j])  # Compute the sum of two numbers directly above
            row.append(1)  # Every row ends with 1
            dp.append(row)  # Add the row to the Pascal's triangle

        return dp