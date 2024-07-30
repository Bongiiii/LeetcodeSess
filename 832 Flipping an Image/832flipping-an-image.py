class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #first flip image using the reverse method, only horizontally, rows
        #then check each elemnt and replace accordingly
        rows, columns = len(image), len(image[0])
        
        for i in range(rows):
            image[i].reverse()

            for j in range(columns):
                image[i][j] = 1 - image[i][j]

        return image