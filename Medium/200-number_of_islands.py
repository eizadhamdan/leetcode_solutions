class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)

        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands
        # time: O(m*n), space: O(m*n)
        