class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Understand:
        input - 2d array of strings and string, output - boolean

        Match:
        dfs/ recursion
        pointers

        Plan:
        initiate a helper function that helps traverse the 2d array,
        movement is only in the horizontal(left and right), vertical(up and  down)
        helper should be mark letters that have been checked so as not to reuse letters
         and avoid infinite loops
        move as long as it's within bounds
        then main function, chheck if current element in array is same as element from pointer, 
        if so increment pointer, move array pointer too and do that by calling recursively the helper
        if you can't form the whole word or even part of the characters by moving, early return false
        otherwise true when word is found

        R/E:
        s/c == O(N), recursive calls
        t/c = O(M*N), we visit all nodes
        """
        def dfsHelper(x, y, index):
           # Check if the last character matches 
            if index == len(word) - 1:
                return board[x][y] == word[index]
            # If current character does not match the word character at index, return False
            if board[x][y] != word[index]:
                return False
            # Store the current character and mark the cell as visited with "0"
            temp = board[x][y]
            board[x][y] = "0"
            # Define directions for exploration: up, right, down, left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            # Loop through all possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # Check boundaries and if the next cell is not visited
                if 0 <= new_x < row and 0 <= new_y < col and board[new_x][new_y] != "0":
                    # Recur with the new position and the next character index
                    if dfsHelper(new_x, new_y, index + 1):
                        return True
            # Restore the current cell's value after exploring all directions
            board[x][y] = temp
            return False
           

        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfsHelper(i,j,0):
                    return True

        return False
        #main function