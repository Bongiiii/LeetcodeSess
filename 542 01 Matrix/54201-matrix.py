from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        # Initialize the queue with all '0' positions and set non-zero cells to -1
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1  # Mark non-zero cells to track cells to update
        
        # Directions for moving in the matrix (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # BFS to update distances
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if the cell is unvisited (-1)
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1  # Update distance
                    queue.append((nr, nc))       # Add updated cell to queue
        
        return mat
