class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            # If out of bounds or at a water cell, return 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            # Mark the cell as visited by setting it to 0
            grid[i][j] = 0
            area = 1  # Current cell

            # Explore all 4 directions
            area += dfs(i + 1, j)  # Down
            area += dfs(i - 1, j)  # Up
            area += dfs(i, j + 1)  # Right
            area += dfs(i, j - 1)  # Left

            return area

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Calculate the area of the current island
                    max_area = max(max_area, dfs(i, j))

        return max_area