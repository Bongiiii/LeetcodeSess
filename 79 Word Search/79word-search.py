class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        U:
        find a word in a cross word puzzle, can only move up, down, L, R
        - one character is to used once/ none reusable

        M:
        dfs
        backtracking
        graph

        P:
        use a pointer to iterate through the characters in the word
        when you find the character in board, then trigger a recursive helper
         func that recursively checks if that word can be made using any neighbouring chars
        so backtracking comes in when we need to know where we stopped and be able to keep
         track of past chars in case we go deep down and then along the way fail,
         we need to explore other options and just backtrack
        
        I:

        R/E:
        s/c = O(n), recursive calls...recursive stack size
        t/c = O(m*n)
        """
        m, n, moves = len(board), len(board[0]), (-1, 0 , 1, 0, -1)

        def dfs(i,j,k): #takes in indices for index in board, and pointer for curr char in word
            #base case when we have finished word
            if k == len(word) - 1:
                return board[i][j] == word[k]

            #chars currently pointed to dont match
            if board[i][j] != word[k]:
                return False

            #preserve curr char
            track = board[i][j]

            #mark as visited
            board[i][j] = "#"

            for row, col in pairwise(moves):
                newR, newC = i + row, j + col

                #check bounds and that cell hasnt been visited
                if (0 <= newR < m) and (0 <= newC < n) and board[newR][newC] != "#":
                    if dfs(newR, newC, k + 1):
                        #update original not new
                        board[i][j] = track
                        return True

            board[i][j] = track
            return False
        
        #define bounds for board
        for r in range(m):
            for c in range(n):
                #recursively check for word in board
                if dfs(r,c,0):
                    return True

        return False