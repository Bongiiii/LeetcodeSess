class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
         # Check if our starting point color needs to be changed: If color is as intended then return original image. Otherwise continue.    
        if (image[sr][sc] == color):
            return image

        # Store our starting point color in a variable. We are given our starting point through the parameters `image`, `sr`, and `sc`. `sr` represents the row, and `sc` represents the column. 
        m, n, originalColor = len(image), len(image[0]), image[sr][sc]

        # Using a dfs call we. can checks its neighbors (left, right, top, bottom), replaces those that had the same number as the one the starting pixel had (which is 1) before it changed to the new color (2). So it changes all the 1s to 2s as long as they are neighbors. Then moves to its left neighbor (1st column) to go through the same process.
        def dfs(i,j):
            # Check if neighbor is inbound and is the same as the orginalColor.
            if i < 0 or i > m-1 or j < 0 or j > n-1 or image[i][j] != originalColor:
                # if it is out of bound or a different color, then stop
                return
            
            # else repeat.
            image[i][j] = color
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # Starts from the middle as the starting pixel, changes itself to the new color which is ‘2’ in this case. And run a dfs call to check and change all it's neighbors.
        dfs(sr, sc)
        
        # Return the doctored image
        return image