from heapq import heappop, heappush

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        Understand:
        input - 2d array/matrix, output - integer

        Match:
        2d matrix
        weighted graph
        min heap(implemented with a priority queue)

        Plan:
        use a minheap to process the cells using bfs
        edit the array in place when you encounter cells to mark as visited to get rid of infinite loop

        R/E:
        s/c = O(r*c)
        t/c =O(r*c*log(rc))
        """
        #dimensions
        rows, cols = len(heightMap), len(heightMap[0])

        #minheap to process every cell in matrix
        minHeap = []
        #add bounds to the minheap
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    heappush(minHeap,(heightMap[r][c],r,c))
                    #mark the bounds as visited
                    heightMap[r][c] = -1


        waterTrapped = 0
        maxHeight = -1

        while minHeap:
            h,r,c = heappop(minHeap)
            maxHeight = max(maxHeight, h)
            waterTrapped += maxHeight - h


            #check neighbors of that cell
            neighbors = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]

            for nr, nc in neighbors:
                #if neighboring cell is out of bounds or already visited skip
                if (nr < 0 or nc < 0 or nr == rows or nc == cols or heightMap[nr][nc] == -1):
                    continue

                #otherwise not yet processed so add to the minheap for processing
                heappush(minHeap,(heightMap[nr][nc],nr,nc))
                #then mark it as visited after adding to heap
                heightMap[nr][nc] = -1


        #when all cells have been processed or no cell left to process
        return waterTrapped