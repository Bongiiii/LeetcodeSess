class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Understand:
        input - square matrix, output - array of arrays
        problem summary: given an array of arrays, rotate it by 90 degrees and return resultant array of arrays

        Match:
        recursion
        array of arrays

        Plan:
        initiate the rows, columns
        since this is a square matrix, iterate in the range of either
        transpose the elements along the leading diagonal
        then reverse matrix


        R/E:
        s/c = O(1), in place transposition
        t/c = O(N^2)

        """
        rows, col = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(i + 1, col):
                #transpose/ swap rows for columns and columns for rows
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #reverse matrix
        for i in range(rows):
            matrix[i].reverse()
       