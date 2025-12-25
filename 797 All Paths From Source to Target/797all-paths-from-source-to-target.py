from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        #using bfs

        #initializing to node 0 as they start from 0 anyway
        q, res, n = deque([[0]]), [], len(graph)

        #find path from 0 - (n-1) as long q - queue is valid
        while q:
            currPath = q.popleft()
            lastNode = currPath[-1]

            #check last node in currpath...if its (n-1) then valid path has been found hence add to res
            if lastNode == (n - 1):
                res.append(currPath)
                continue

            else:
                for neighbor in graph[lastNode]:
                    newPath = currPath + [neighbor]
                    q.append(newPath)

        return res