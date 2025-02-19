class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Understand:
        input - 2d array of integers, output - array of integers

        Match:
        simulation
        2d array manipulation
        graphs/dfs

        Plan:
        start from 0,0 and continue moving clockwise unless you get out of bounds, or 
        initialize an array for the spiral list and visited set

        R/E:
        s/c = t/c = O(m*n)
        """

         # Define matrix dimensions.
        rows, cols = len(matrix), len(matrix[0])
      
        # Define directions for spiral movement (right, down, left, up).
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
      
        # Initialize row and column indices and the direction index.
        row = col = direction_index = 0
      
        # Initialize the answer list and a set to keep track of visited cells.
        result = []
        visited = set()
      
        # Iterate over the cells of the matrix.
        for _ in range(rows * cols):
            # Append the current element to the result list.
            result.append(matrix[row][col])
            # Mark the current cell as visited.
            visited.add((row, col))
          
            # Calculate the next cell's position based on the current direction.
            next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]
          
            # Check if the next cell is within bounds and not visited.
            if not (0 <= next_row < rows) or not (0 <= next_col < cols) or (next_row, next_col) in visited:
                # Change direction if out of bounds or cell is already visited.
                direction_index = (direction_index + 1) % 4
          
            # Update the row and column indices to the next cell's position.
            row += directions[direction_index][0]
            col += directions[direction_index][1]
      
        # Return the result list.
        return result