class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Initialize a variable to keep track of the number of battleships
        numberOfBattleships = 0
        
        # Iterate over the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                # If a 'X' is seen and if the left side and the up side is ocean or at the boarder, then it's the head of a ship and add one to the count.
                if cell == "X":
                    if (i == 0 or board[i - 1][j] == ".") and\
                       (j == 0 or board[i][j - 1] == "."):
                            numberOfBattleships += 1
        
        # Return number of battleships
        return numberOfBattleships