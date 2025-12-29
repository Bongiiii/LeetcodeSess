from itertools import pairwise

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        U:
        input - an array of arrays of characters, a string
        output - boolean

        prob summary: determine if there are valid paths to find the word given the board.

        M:
        graph
        dfs
        backtracking
        pointers approach

        P:
        use pointer to keep track of characters in word
        use dfs to check for valid characters to make word moving either horizontally or vertically
        remember to mark and unmark to ensure full exploration of potential paths
        base cases: early termination

        I:

        R:

        E:
        s/c = O(L), length of word...the potential length(depth rather) of the recursive stack
        t/c = O(m*n*L)
        """
        rows, cols, directions = len(board), len(board[0]), (-1,0,1,0,-1)

        def dfs(i,j,k):
            #base case
            if k == len(word) - 1:
                return board[i][j] == word[k]

            if board[i][j] != word[k]:
                return False

            og_char = board[i][j]
            board[i][j] = "?"

            for cur_row, cur_col in pairwise(directions):
                new_row, new_col = cur_row + i, cur_col + j

                if (0<=new_row<rows) and (0<=new_col<cols) and board[new_row][new_col] != "?":
                    if dfs(new_row, new_col, k+1):
                        board[i][j] = og_char
                        return True

            board[i][j] = og_char
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True

        return False