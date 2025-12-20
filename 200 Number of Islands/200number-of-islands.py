from collections import deque
from itertools import pairwise

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS approach/ iterative approach
        """
        rows, cols, islandCount, travelDirections = len(grid), len(grid[0]), 0, (-1, 0, 1, 0, -1)
        
        #base case unnecessary since constraints guarranteed presence of grid with either 0s or 1s
        # if not grid or not grid[0]:
        #     return 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1":
                    islandCount += 1

                    #add that cell and its neighbors to queue
                    queue = deque([(row, col)])
                    #sink that cell/ mark as visited
                    grid[row][col] = "2"

                    while queue:
                        rq, cq = queue.popleft()

                        for r,c in pairwise(travelDirections):
                            nrow, ncol = rq + r, cq + c

                            if 0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol] == "1":
                                grid[nrow][ncol] = "2"
                                queue.append((nrow, ncol))


        return islandCount