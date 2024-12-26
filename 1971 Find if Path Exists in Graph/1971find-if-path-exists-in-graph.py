class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        dfs, recursion
        """
        #helper function to map node to parent node
        def findRoot(node):
            if parent[node] != node:
                parent[node] = findRoot(parent[node])
            return parent[node]

        parent = list(range(n))#creates an array 0 to n-1 inclusive

        for start, end in edges:
            parent[findRoot(start)] = findRoot(end)

        return findRoot(source) == findRoot(destination)
        