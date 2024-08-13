class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        r_range = range(ROWS)
        c_range = range(COLS)

        def dfs(r, c, ocean, maxHeight):
            if r not in r_range or c not in c_range:
                return
            if (r, c) in ocean:
                return
            if heights[r][c] < maxHeight:
                return
            ocean.add((r, c))
            curr_height = heights[r][c]

            dfs(r + 1, c, ocean, curr_height)
            dfs(r - 1, c, ocean, curr_height)
            dfs(r, c - 1, ocean, curr_height)
            dfs(r, c + 1, ocean, curr_height)

        atlantic, pacific = set(), set()

        for c in c_range:
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)

        for r in r_range:
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)

        output = []
        for coord in pacific:
            if coord in atlantic:
                output.append([coord[0], coord[1]])
        return output
