class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #transpose, swap rows for columns and columns for rows across the leading diagonal leaving the elements on the diagonal constant

        # Create empty array
        result = []
        # Create row for each column
        for j in range(len(matrix[0])):
            result.append([])
            # Get each element from same column and insert into row
            for i in range(len(matrix)):
                result[j].append(matrix[i][j])
        # Return result
        return result