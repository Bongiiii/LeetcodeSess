class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Understand:
        input - string and integer, output - string
        Problem summary: given a string, convert it into zigzag

        Match:
        simulation
        strings
        arrays(2d)

        Plan:
        initialize a string for the result, also initiate a 2d array of dimensions, r = number of rows, and columns is half the length of string
        iterate through the initial string, 
        fill the matrix in the zig zag way, first down and then going up diagonally, 
        have bounds not to go out of 
        then after filling the matrix in a zigzag fashion
        then use bfs(start from the first row top element going to the right, always start at the left - right), joing elements 
        into the final string and return the string, in cells with no character just ignore

        R/E:
        s/c = O(N), n = r by c of the matrix 
        t/c = O(N), overall time complexity is O(N)
        """
    
        # Edge case: if only one row, no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # List of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Build the zigzag pattern row by row
        for char in s:
            rows[current_row] += char
            # Change direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final result
        return ''.join(rows)
