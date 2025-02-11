from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Directions for moving in 4 directions (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Queue for BFS
        queue = deque()
        # Count of fresh oranges
        fresh_oranges = 0
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        # If no fresh oranges, no need to do anything
        if fresh_oranges == 0:
            return 0
        
        minutes_passed = 0
        
        # BFS to spread the rot
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        queue.append((nx, ny))
            minutes_passed += 1
        
        # If there are still fresh oranges left, return -1
        return minutes_passed - 1 if fresh_oranges == 0 else -1

